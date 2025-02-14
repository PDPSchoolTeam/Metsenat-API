from django.urls import path
from .views import RegisterAPIView, LoginAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),  # for JWT token generation
    path('login', LoginAPIView.as_view(), name='login'),
]
