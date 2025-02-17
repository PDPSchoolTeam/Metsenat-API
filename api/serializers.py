from rest_framework import serializers
from .models import User, University, Student, Sponsor

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'role', 'first_name', 'last_name', 'avatar']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'degree', 'contract_price', 'university']

class SponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = "__all__"