from django.shortcuts import render
from mongoengine import DoesNotExist
# Create your views here.


from .serializers import StudentSerializer
from .models import Student
from rest_framework_mongoengine import generics
from django.http import HttpResponse, JsonResponse
import logging

logging.basicConfig(filename="Logging.txt", filemode="a", level=logging.INFO)


# createing  theStudents
class CreateStudent(generics.CreateAPIView):
    try:
        serializer_class = StudentSerializer
        logging.info(" new Student is created sucessfully...")

    except Exception as e:
        logging.error(f"error occured", e)


# getting all theStudents
class StudentList(generics.ListAPIView):
    try:
        StudentSerializer.Meta.model = Student
        serializer_class = StudentSerializer
        queryset = Student.objects.all()
    except Exception as e:
        logging.error(f"error occured", e)

def get_queryset(self):
    queryset = self.queryset
    return queryset


class GetStudentById(generics.RetrieveAPIView):
    serializer_class = StudentSerializer
    lookup_field = "pk"
    # queryset=Student.objects.all()
    

    # def get_queryset(self):
        
    #    queryset=Student.objects.get(pk=self.kwargs[self.lookup_field])
    
    #     return queryset
    
    def get_object(self):
        try:
            queryset = self.get_queryset()
            if queryset is None:
                return 'Does not Exists'
            # student = queryset.get(pk=self.kwargs[self.lookup_field])
            return queryset
            print(student)
            if student is None:
                return "error1"
                raise DoesNotExist
            return student
        
      
        except Exception as e:
            logging.error(f"Failed to retrieve document")
            print("error",e)
            
            