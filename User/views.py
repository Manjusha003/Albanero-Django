from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.


# class RegisterUser(APIView):
#     def post(self,request):
#         serializer = UserSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response({"status": 403, "error": serializer.errors})
#         serializer.save()
#         user=User.objects.get(username=serializer.data)
#         return Response({"status": 200, "payload": serializer.data})

class StudentAPIView(APIView):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response({"status": 200, "payload": {"data": serializer.data}})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status": 403, "error": serializer.errors})
        serializer.save()
        return Response({"status": 200, "payload": serializer.data})

    def put(self, request):
        try:
            student=Student.objects.get(id=request.data['id'])
            serializer=StudentSerializer(student,data=request.data,partial=True)
            if not serializer.is_valid():
                return Response({"status":403,"error":serializer.errors})
            serializer.save()
            return Response({"status":200,"payload":serializer.data})
        except Exception as e:
            return Response({"status":403,"message":"Invalid Id"})

    

    def patch(self, request):
        try:
            student=Student.objects.get(id=request.data['id'])
            serializer=StudentSerializer(student,data=request.data,partial=False)
            if not serializer.is_valid():
                return Response({"status":403,"error":serializer.errors})
            serializer.save()
            return Response({"status":200,"payload":serializer.data})
        except Exception as e:
            return Response({"status":403,"message":"Invalid Id"})

    def delete(self, request):
        try:
            id=request.GET.get('id')
            student=Student.objects.get(id=id)
            student.delete()
            return Response({"status":200,"message":"User deleted Successfully"})
        
        except Exception as e:
            return Response({"status":403,"message":"Invalid Id"})
