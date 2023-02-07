from rest_framework_mongoengine import serializers
from .models import Student


class StudentSerializer(serializers.DocumentSerializer):
    
    class Meta:
        model = Student
        fields = "__all__"

    