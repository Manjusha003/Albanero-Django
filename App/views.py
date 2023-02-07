from django.shortcuts import render
from mongoengine import DoesNotExist
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response



# Create your views here.


from .serializers import StudentSerializer
from .models import Student
from rest_framework_mongoengine import generics

import logging

logging.basicConfig(filename="Logging.txt", filemode="a", level=logging.INFO)


# createing  theStudents
class CreateStudent(generics.CreateAPIView):
    try:
        serializer_class = StudentSerializer
        logging.info(" new Student is created sucessfully...")

    except Exception as e:
        logging.error(f"error occured", e)


# getting all the Students
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
    StudentSerializer.Meta.model=Student
    serializer_class = StudentSerializer
    students=Student.objects.all()
    serializer=StudentSerializer(students,many=True)
    lookup_field = "pk"

    def get_queryset(self):
    #   try:
        queryset=Student.objects.get(pk=self.kwargs[self.lookup_field])
        serializer=self.serializer_class(queryset,many=True)
        return queryset
    #   except DoesNotExist:
    #       return JsonResponse({'message': 'The tutorial does not exist'})

    def get_object(self):
        try:
            queryset=self.get_queryset()
            serializer=self.serializer_class(queryset,many=True)
            if queryset is None:
                raise DoesNotExist
            return queryset
        except DoesNotExist:
            return FileNotFoundError('File not found')
            # return HttpResponse('Doc not found')
    # queryset=Student.objects.all()



## updating the student details by using id

class UpdateStudentDetails(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field="pk"

    @csrf_exempt
    def update_items(request, pk):
       student = Student.objects.get(pk=pk)
       data = StudentSerializer(instance=student, data=request.data)
       if data.is_valid():
          data.save()
          return Response(data.data)
       else:
          return Response({"message":"error"})
       

class DeleteStudent(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field="pk"

    def delete_student(request,pk):
        student =Student.objects.get(pk=pk)
        if student is None:
          logging.error(f"error occured")
          return Response({"message":"student is not exist with given id"})
        else:
            student.delete()
            logging.info({"message":"student is not exist with given id"})
            return Response({"message":"Student deleted successfully..."})



  




