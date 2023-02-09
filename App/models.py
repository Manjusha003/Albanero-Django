from django.db import models
from rest_framework.exceptions import ValidationError

# Create your models here.

from mongoengine import Document, SequenceField, StringField, EmailField,IntField


class Student(Document):
    studentId = SequenceField(primary_key=True)
    name = StringField(max_length=50)
    email= EmailField(required=True,unique=True)
    password = StringField(required=True, max_length=50)
    age=IntField(default=20)
    

    def clean(self):
        if self.name:
            for n in self.name:
                if n.isdigit():
                    raise ValidationError("name cananot be numeric value ")
        elif self.age<18:
            raise ValidationError("age cannot be less than 18 ")
