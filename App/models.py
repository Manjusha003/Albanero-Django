from django.db import models

# Create your models here.

from mongoengine import Document, SequenceField, StringField, EmailField,IntField


class Student(Document):
    studentId = SequenceField(primary_key=True)
    name = StringField(required=True, max_length=50)
    email= EmailField(required=True,unique=True)
    password = StringField(required=True, max_length=50)
    age=IntField(default=20)
    
    
