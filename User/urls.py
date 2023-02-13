
from django.urls import path
from .views import StudentAPI

urlpatterns = [
    
    # path("register", RegisterView.as_view()),
    path("api/user",StudentAPI.as_view()),
    
    
]