from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .serializers import (LoginSerializer,
                          RegisterSerializer,
                          SponsorsSerializer,
                          SponsorDeleteSerializer,
                          StudentsSponsorsSerializer,
                          StudentSerializer,

                          )
from .models import User, Sponsor, Student
from rest_framework.parsers import MultiPartParser, FormParser


class RegisterAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @extend_schema(
        summary="User Registration",
        description="Register a new user",
        request=RegisterSerializer,  # Correctly specify the request body
        responses={
            201: OpenApiResponse(response=RegisterSerializer, description="JWT access token and refresh token"),
            400: OpenApiResponse(description="Invalid input data")
        },
        tags=["User Authentication API"]
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(password=make_password(serializer.validated_data['password']))
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": access_token
                }, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @extend_schema(
        summary="User Login",
        description="Login user with email and password",
        request=LoginSerializer,
        responses={
            200: OpenApiResponse(response=LoginSerializer, description="JWT access token and refresh token"),
            400: OpenApiResponse(description="Invalid credentials")
        },
        tags=["User Authentication API"]
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                user_obj = User.objects.get(email=user)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            if user_obj and check_password(password, user_obj.password):
                refresh = RefreshToken.for_user(user_obj)
                access_token = str(refresh.access_token)

                return Response(
                    {
                        "refresh": str(refresh),
                        "access": access_token
                    }, status=status.HTTP_200_OK
                )
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# class UniversityAPIView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#
#     @extend_schema(
#         summary="University List",
#         description="University List API Views",
#         tags=["University API"],
#         responses={200: SponsorsSerializer}
#     )
#     def get(self, request):
#         try:
#             universities = University.objects.all()
#             serializer = UniversitySerializer(universities, many=True)
#             return Response(serializer.data)
#         except University.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
# class UniversityDetailsAPIView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#
#     @extend_schema(
#         summary="University Details",
#         description="University Details API Views",
#         tags=["University API"],
#         responses={200: SponsorsSerializer}
#     )
#     def get(self, request):
#         universities = University.objects.all()
#         serializer = UniversitySerializer(universities, many=True)
#         return Response(serializer.data)

class SponsorsAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @extend_schema(
        summary="Sponsors List",
        description="Sponsors List API Views",
        tags=["Sponsor API"],
        responses={200: SponsorsSerializer}
    )
    def get(self, request):
        try:
            sponsors = Sponsor.objects.all()
            serializer = SponsorsSerializer(sponsors, many=True)
            return Response(serializer.data)
        except Sponsor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class SponsorDetailsAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @extend_schema(
        summary="Sponsor Details",
        description="Sponsor Details API Views",
        tags=["Sponsor API"],
        responses={200: SponsorsSerializer}
    )
    def get(self, request, pk):
        try:
            sponsor = Sponsor.objects.get(pk=pk)
            serializer = SponsorsSerializer(sponsor)
            return Response(serializer.data)
        except Sponsor.DoesNotExist:
            return Response({'detail': 'Sponsor not found'}, status=status.HTTP_404_NOT_FOUND)

class SponsorCreateAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @extend_schema(
        summary="Sponsor Registration",
        description="Register a new sponsor",
        request=SponsorsSerializer,  # Correctly specify the request body
        responses={
            201: OpenApiResponse(response=SponsorsSerializer, description="JWT access token and refresh token"),
            400: OpenApiResponse(description="Invalid input data")
        },
        tags=["Sponsor API"]
    )
    def post(self, request):
        serializer = SponsorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SponsorUpdateAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @extend_schema(
        summary="Sponsor Update",
        description="Sponsor Update API View",
        request=SponsorsSerializer,  # Correctly specify the request body
        responses={
            200: OpenApiResponse(response=SponsorsSerializer, description="JWT access token and refresh token"),
            400: OpenApiResponse(description="Invalid input data")
        },
        tags=["Sponsor API"]
    )
    def put(self, request, pk):
        sponsor = get_object_or_404(Sponsor, pk=pk)
        serializer = SponsorsSerializer(sponsor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SponsorDeleteAPIView(APIView):
    @extend_schema(
        summary="Sponsor Delete",
        description="Sponsor API Delete",
        tags=["Sponsor API"]
    )
    def delete(self, request, pk):
        sponsor = get_object_or_404(Sponsor, pk=pk)
        sponsor.delete()
        return Response({'message': 'Sponsor has been deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    serializer_class = SponsorDeleteSerializer

class StudentsSponsorsAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @extend_schema(
        summary="Student Sponsor Create",
        description="Student Sponsors API View",
        request=StudentsSponsorsSerializer,  # Correctly specify the request body
        responses={
            201: OpenApiResponse(response=StudentsSponsorsSerializer, description="Sponsors has been helped for student's contacts successfully created"),
            400: OpenApiResponse(description="Invalid input data")
        },
        tags=["Sponsor API"]
    )
    def post(self, request):
        serializer = StudentsSponsorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    @extend_schema(
        summary="Student List",
        description="Student List API Views",
        tags=["Student API"],
        responses={200: StudentSerializer}
    )
    def get(self, request):
        try:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
