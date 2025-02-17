from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .serializers import LoginSerializer, RegisterSerializer, UniversitySerializer, SponsorsSerializer
from .models import User, University, Sponsor
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
        tags=["User Authentication"]
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
        tags=["User Authentication"]
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


class UniversityAPIView(APIView):
    @extend_schema(
        summary="University List",
        description="Retrieves a list of all universities.",
        tags=["University"],
        responses={200: UniversitySerializer(many=True)}
    )
    def get(self, request):
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data)


class SponsorDetailsAPIView(APIView):
    @extend_schema(
        summary="Sponsor Details",
        description="Sponsor Details API Views",
        tags=["Sponsor Details"],
        responses={200: SponsorsSerializer}
    )
    def get(self, request, pk):
        try:
            sponsor = Sponsor.objects.get(pk=pk)
            serializer = SponsorsSerializer(sponsor)
            return Response(serializer.data)
        except Sponsor.DoesNotExist:
            return Response({'detail': 'Sponsor not found'}, status=status.HTTP_404_NOT_FOUND)
