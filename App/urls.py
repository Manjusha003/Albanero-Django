from django.urls import path


from .views import StudentList,UpdateModelView,DeleteStudent,RegisterView,LoginView
urlpatterns = [
    path('register',RegisterView.as_view(),name="student_register"),
    path('login',LoginView.as_view()),
    path("api/users",StudentList.as_view(),name='student_list'),
    path("api/user/update/<int:pk>",UpdateModelView.as_view(),name="update_student"),
    path("api/user/delete/<int:pk>",DeleteStudent.as_view()),
   
]