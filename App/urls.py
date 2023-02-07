from django.urls import path

from .views import CreateStudent,StudentList,GetStudentById

urlpatterns = [
    
    path("createuser", CreateStudent.as_view()),
    path("api/users",StudentList.as_view()),
    path("api/user/<int:pk>",GetStudentById.as_view())
    
]