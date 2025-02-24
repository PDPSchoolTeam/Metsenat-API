from django.db.models import Sum
from rest_framework import serializers
from .models import User, University, Student, Sponsor, StudentSponsor, TotalPayment


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

class StudentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = []

class TotalPaymentsSerializer(serializers.ModelSerializer):
    total_paid = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_requested = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_needed = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = TotalPayment
        fields = ['total_paid', 'total_requested', 'total_needed']

    def __init__(self, *args, **kwargs):
        total_paid = Sponsor.objects.aggregate(total_paid=Sum('amount'))['total_paid'] or 0
        total_requested = Student.objects.aggregate(total_requested=Sum('contract_price'))['total_requested'] or 0
        total_needed = total_requested - total_paid
        kwargs['context'] = {'total_paid': total_paid, 'total_requested': total_requested, 'total_needed': total_needed}
        super().__init__(*args, **kwargs)

    def get_total_paid(self, obj):
        return self.context.get('total_paid', 0)

    def get_total_requested(self, obj):
        return self.context.get('total_requested', 0)

    def get_total_needed(self, obj):
        return self.context.get('total_needed', 0)
