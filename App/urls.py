from django.urls import path


from .views import StudentList,UpdateModelView,DeleteStudent,RegisterView,LoginView
urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path("api/users",StudentList.as_view()),
    path("api/user/update/<int:pk>",UpdateModelView.as_view()),
    path("api/user/delete/<int:pk>",DeleteStudent.as_view()),
   
]