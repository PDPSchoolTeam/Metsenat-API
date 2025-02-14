from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .serializers import LoginSerializer, RegisterSerializer
from .models import User

class RegisterAPIView(APIView):
    @extend_schema(
        summary="User Registration",
        description="Register user",
        request=RegisterSerializer,
        responses={
            200: OpenApiParameter(name="Tokens", description="JWT access token and refresh tokens"),
            400: OpenApiParameter(name="Errors", description="Invalid credentials")
        },
        tags=["User Authentication"]
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(password=make_password(serializer.validated_data['password']))
            # Generate JWT token
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
    @extend_schema(
        summary="User Login",
        description="Login user with email and password",
        request=LoginSerializer,
        responses={
            200: OpenApiParameter(name="Tokens", description="JWT access token and refresh tokens"),
            400: OpenApiParameter(name="Errors", description="Invalid credentials")
        },
        tags=["User Authentication"]
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['email']
            password = serializer.validated_data['password']
            if user and check_password(password, User.objects.get(email=user).password):
                # Generate JWT token
                refresh = RefreshToken.for_user(User.objects.get(email=user))
                access_token = str(refresh.access_token)

                return Response(
                    {
                        "refresh": str(refresh),
                        "access": access_token
                    }, status=status.HTTP_200_OK
                )
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)