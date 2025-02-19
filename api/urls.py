from django.urls import path
from .views import (
    RegisterAPIView,
    LoginAPIView,
    # UniversityAPIView,
    # UniversityDetailsAPIView,
    SponsorsAPIView,
    SponsorDetailsAPIView,
    SponsorCreateAPIView,
    SponsorUpdateAPIView,
    SponsorDeleteAPIView
)

app_name = 'api'

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),  # for JWT token generation
    path('login', LoginAPIView.as_view(), name='login'),
    # path('university', UniversityAPIView.as_view(), name='universities-list'),  # for University View
    # path('university/<int:pk>', UniversityDetailsAPIView.as_view(), name='university-details'),  # for University List
    path('sponsors', SponsorsAPIView.as_view(), name='sponsors-list'),  # for Sponsors List API View
    path('sponsor/<int:pk>', SponsorDetailsAPIView.as_view(), name='sponsor-detail'),  # for Sponsor Detail View
    path('sponsor/create', SponsorCreateAPIView.as_view(), name='sponsor-create'),  # for Sponsors Create View
    path('sponsor/update/<int:pk>', SponsorUpdateAPIView.as_view(), name='sponsor-update'),  # for Sponsors Update View
    path('sponsor/delete/<int:pk>', SponsorDeleteAPIView.as_view(), name='sponsor-delete'),  # for Sponsors Delete View

]
