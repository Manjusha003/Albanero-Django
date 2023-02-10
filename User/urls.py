
from django.urls import path
from .views import StudentAPIView

urlpatterns = [
    
    # path("register", StudentAPIView.as_view()),
    path("api/user",StudentAPIView.as_view()),
    # path("api/user/update/<int:pk>",get_users.as_view()),
    # path("api/user/delete/<int:pk>",delete_user.as_view())
    
]