from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UniversityAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),  # for JWT token generation
    path('login', LoginAPIView.as_view(), name='login'),
    path('university', UniversityAPIView.as_view(), name='universities-list'), # for University View

]
