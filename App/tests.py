
from rest_framework import status
import unittest
from .serializers import StudentSerializer
import requests
from .models import Student

class StudentTestacase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    student = Student(
            name="Manjusha", email="manjusha093@gmail.com", password="12345", age=22
        )
    student.save()

    new_student={
        "name":"Manju",
        "email":"manju021@gmail.com",
        "password":"6789",
        "age":23
    }
    student_serializer = StudentSerializer(data=new_student)


    def test_register(self):
        if self.student_serializer.is_valid():
            self.student_serializer.create(self.new_student)
        self.assertEqual(Student.objects.count(),1)
    
    def test_student(self):
        self.student.update(set__name="Raut")
        self.assertEqual(
            Student.objects.get(name="Manjusha").name, "Manjusha"
        )
        
    def test_delete(self):
        self.student.delete()
        self.assertEqual(Student.objects.count(),0)


   
    @classmethod
    def tearDownClass(cls):
        Student.drop_collection()

if __name__ == "__main__":
 unittest.main() # run all tests
