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
    SponsorDeleteAPIView,
    StudentsSponsorsAPIView,
    StudentAPIView,
    StudentCreateAPIView,
    StudentUpdateAPIView,
    StudentDeleteAPIView,
    SponsorFilterAPIView,
    StudentFilterAPIView,
    StudentSponsorFilterAPIView,
    TotalPaymentsAPIView
)

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
    path('sponsor/filter', SponsorFilterAPIView.as_view(), name='sponsor-filter'),  # for Sponsors Filter View
    path('sponsor/student', StudentsSponsorsAPIView.as_view(), name='sponsor-student'),  # for Students with Sponsors
    path('sponsor/student/filter', StudentSponsorFilterAPIView.as_view(), name='sponsor-student-filter'),
    # for StudentSponsor Filter View
    path('student', StudentAPIView.as_view(), name='student-list'),  # for Student List View
    path('student/create', StudentCreateAPIView.as_view(), name='student-create'),  # for Student Create View
    path('student/update/<int:pk>', StudentUpdateAPIView.as_view(), name='student-update'),  # for Student Update View
    path('student/delete/<int:pk>', StudentDeleteAPIView.as_view(), name='student-delete'),  # for Student Delete View
    path('student/filter', StudentFilterAPIView.as_view(), name='student-filter'),  # for Student Filter View
    path('total-payment', TotalPaymentsAPIView.as_view(), name='total-payment'), # for Total Payment View
]
