from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import CreateStudent,StudentList,GetStudentById,UpdateStudentDetails,DeleteStudent

urlpatterns = [
    
    path("createuser", CreateStudent.as_view()),
    path("api/users",StudentList.as_view()),
    path("api/user/<int:pk>",GetStudentById.as_view()),
    path("api/user/update/<int:pk>",csrf_exempt(UpdateStudentDetails.as_view())),
    path("api/user/delete/<int:pk>",DeleteStudent.as_view())
    
]