from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class StudentAPI(APIView):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response({"status": 200, "payload": {"data": serializer.data}})

    def post(self, request):
        try:
            serializer = StudentSerializer(data=request.data)
            
            if not serializer.is_valid():
                return Response({"status": 403, "error": serializer.errors})
            print("Hi")
            serializer.save()
            return Response({"message": "Student is created successfully", "payload":{"data":serializer.data}},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"data": "data"},status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request):
    #     try:
    #         student = Student.objects.get(id=request.data["id"])
    #         serializer = StudentSerializer(student, data=request.data, partial=True)
    #         if not serializer.is_valid():
    #             return Response({"status": 403, "error": serializer.errors})
    #         serializer.save()
    #         return Response({"status": 200, "payload": serializer.data})
    #     except Exception as e:
    #         return Response({"status": 403, "message": "Invalid Id"})

    # def patch(self, request):
    #     try:
    #         student = Student.objects.get(id=request.data["id"])
    #         serializer = StudentSerializer(student, data=request.data, partial=False)
    #         if not serializer.is_valid():
    #             return Response({"status": 403, "error": serializer.errors})
    #         serializer.save()
    #         return Response({"status": 200, "payload": serializer.data})
    #     except Exception as e:
    #         return Response({"status": 403, "message": "Invalid Id"})

#     def delete(self, request):
#         try:
#             id = request.GET.get("id")
#             student = Student.objects.get(id=id)
#             student.delete()
#             return Response({"status": 200, "message": "User deleted Successfully"})

#         except Exception as e:
#             return Response({"status": 403, "message": "Invalid Id"})


# class StudentAPI(APIView):
#     def get(self,request):
#         return Response({"message":"get all students"})