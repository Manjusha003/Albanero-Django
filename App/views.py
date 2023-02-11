from django.shortcuts import render
from mongoengine import DoesNotExist
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework_mongoengine import generics
import logging
from rest_framework.views import APIView
from rest_framework import status
import jwt

logging.basicConfig(filename="Logging.txt", filemode="a", level=logging.INFO)


class RegisterView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = StudentSerializer(data=data)

            if not serializer.is_valid():
                return Response(
                    {"data": serializer.errors, "message": "Something went wrong"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            serializer.save()
            return Response(
                {
                    "message": "Student Created successfully",
                    "payload": {
                        "data": serializer.data,
                    },
                    "success": "true",
                }
            )
        except Exception as e:
            return Response(
                {"message": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(generics.GenericAPIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            user = Student.objects.get(email=email)
            if user.password == password:
                payload = {"email": email}
                jwt_token = {"token": jwt.encode(payload, "SECRET_KEY")}
                return Response(jwt_token, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
                )
        except Student.DoesNotExist:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
            )




class StudentList(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get(self, request):
        group_by=request.GET.get("groupBy")
        if group_by is not None:
            group = [
            {"$group": {"_id": f"${group_by}", "name": {"$push": "$name"}}},
            {"$project": {group_by: "$_id", "_id": 0, "name": "$name"}},
            {"$sort": {"age": -1}},
        ]
            agregated_data = Student.objects.aggregate(*group)
            agregated_list=list(agregated_data)
            return Response(
              {
                "message": "Student information fetched successfully",
                "payload": {
                    "data": agregated_list,
                    "totalCount": Student.objects.count(),
                },
                "success": "true",
              }
            )

        page = int(request.GET.get("page", 1))
        page_size = int(request.GET.get("pageSize", 1))
        order_by = request.GET.get("orderBy")
        start = (page - 1) * page_size
        end = page * page_size

        if page is not None:
          if page_size is not None:
            students = Student.objects.skip(start).limit(end)
            serializer = StudentSerializer(students, many=True)
          
        if order_by is not None:
            students = Student.objects.order_by(order_by)
            serializer = StudentSerializer(students, many=True)


        serializer = StudentSerializer(students, many=True)
        return Response(
            {
                "message": "Student information fetched successfully",
                "payload": {
                    "data": serializer.data,
                    "totalCount": Student.objects.count(),
                },
                "success": "true",
            }
        )


class UpdateModelView(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(
                {"error": "The model instance does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

    def put(self, request, pk):
        model = self.get_object(pk)
        serializer = StudentSerializer(model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Student information updated successfully",
                    "payload": {
                        "data": serializer.data,
                    },
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteStudent(APIView):
    def delete(self, request, pk):
        student = Student.objects.get(pk=pk)
        if student is None:
            logging.error(f"error occured")
            return Response({"detail": "student is not exist with given id"})
        else:
            student.delete()
            logging.info({"message": "student is not exist with given id"})
            return Response(
                {"message": "Student deleted successfully..."},
                status=status.HTTP_204_NO_CONTENT,
            )
