from rest_framework import serializers
from .models import User, University, Student, Sponsor, StudentSponsor

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password', 'role']

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

# class UniversitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = University
#         fields = ['id', 'name']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'degree', 'allocated_money', 'contract_price', 'university']

class SponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ["id", "full_name", "phone_number", "amount", "custom_amount", "deposit_money", "is_organization", "organization_name", "progress"]

class SponsorDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = []

class StudentsSponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = "__all__"