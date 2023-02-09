from rest_framework_mongoengine import serializers
from .models import Student

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class StudentSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        



