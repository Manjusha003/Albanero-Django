from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import BasePermission
from rest_framework import exceptions
from .models import Student
from mongoengine import DoesNotExist
import logging


logging.basicConfig(filename="middlewarelogs.txt", filemode="a", level=logging.INFO)


URL=['/register','/login','api/users']

class StudentAuthMiddleware(BasicAuthentication):
    def authenticate(self, request):
        if request.path in URL:
            return None
        
        email=request.GET.get("email")
        password=request.GET.get("password")

        if not email or not password:
            print("email or password is not sent")
            raise exceptions.AuthenticationFailed("Email or password is missing")
           
        try:
            student=Student.objects.get(email=email,password=password)
            logging.info("student is authenticated..")
            print(student)

        except DoesNotExist:
            raise exceptions.NotAuthenticated("Wrong password or email")
        
        return None
    
class StudentAuthorization(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.path in URL:
                return None
            email=request.GET.get("email")
            password=request.GET.get("password")
            student=Student.objects.get(email=email,password=password,pk=view.kwargs.get("pk"))
            if student:
                return None
        except DoesNotExist:
            raise exceptions.NotAuthenticated("student is not Authorized")







class StudentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        print("middleware before")
        response = self.get_response(request)
        print("middlware after")
        return response



