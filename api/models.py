from decimal import Decimal
from django.db import models, transaction
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from api.managers import UserManager
from django.core.exceptions import ValidationError


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('admin', 'Administrator'),
        ('sponsor', 'Sponsor'),
    ]

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatar/student", default="../media/avatar/student/default-student.webp")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class University(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'university'
        verbose_name_plural = 'universities'


class Student(models.Model):
    class StudentTypes(models.TextChoices):
        BACHELOR = "bachelor"
        MASTER = "master"

    full_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=50, choices=StudentTypes.choices)
    contract_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    allocated_money = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    university = models.ForeignKey("api.University", on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'


class Sponsor(models.Model):
    class StatusChoices(models.TextChoices):
        NEW = 'YANGI', 'Yangi'
        IN_PROCESS = 'Moderatsiyada', 'Moderatsiyada'
        CONFIRMED = 'Tasdiqlangan', 'Tasdiqlangan'
        CANCELLED = 'Bekor qilingan', 'Bekor qilingan'

    class AmountChoice(models.TextChoices):
        MILLION = "1_000_000", "1 000 000"
        FIVE_MILLION = "5_000_000", "5 000 000"
        SEVEN_MILLION = "7_000_000", "7 000 000"
        TEN_MILLION = "10_000_000", "10 000 000"
        THIRTY_MILLION = "30_000_000", "30 000 000"
        OTHERS = "Boshqa", "OTHERS"

    class SponsorStatus(models.TextChoices):
        JURIDICAL = 'YURIDIK SHAXS', 'Yuridik shaxs'
        INDIVIDUAL = 'JISMONIY SHAXS', 'Jismoniy shaxs'

    full_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=30, unique=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)  # Now a DecimalField
    custom_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    deposit_money = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal(0))
    is_organization = models.BooleanField()
    progress = models.CharField(max_length=30, choices=StatusChoices.choices)
    sponsor_status = models.CharField(max_length=50, choices=SponsorStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    organization_name = models.CharField(max_length=250, blank=True, null=True)
    spent_amount = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal(0))

    def save(self, *args, **kwargs):
        self.sponsor_status = self.SponsorStatus.JURIDICAL if self.is_organization else self.SponsorStatus.INDIVIDUAL
        if not self.is_organization:
            self.organization_name = None
        if self.amount == Decimal(0) and self.custom_amount:
            self.amount = self.custom_amount
        elif self.amount != Decimal(0) and self.custom_amount:
            self.custom_amount = None

        self.deposit_money = self.amount

        super().save(*args, **kwargs)

    def clean(self):
        if self.is_organization and not self.organization_name:
            raise ValidationError({'organization_name': "Yuridik shaxs uchun tashkilot nomi majburiy!"})
        if not self.is_organization and self.organization_name:
            raise ValidationError({'organization_name': "Jismoniy shaxs uchun tashkilot nomi kiritilmasligi kerak!"})

    def __str__(self):
        return f"{self.full_name}, {self.sponsor_status}"

    class Meta:
        verbose_name = 'sponsor'
        verbose_name_plural = 'sponsors'


class StudentSponsor(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal(0))
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        with transaction.atomic():
            sponsor = self.sponsor
            sponsor.spent_amount += self.amount
            sponsor.amount -= self.amount
            sponsor.save()

            student = self.student
            student.allocated_money += self.amount
            student.save()

            super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'student sponsor'
        verbose_name_plural = 'student sponsors'


class TotalPayment(models.Model):
    pass
