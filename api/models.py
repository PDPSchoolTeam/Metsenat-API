from django.db import models
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
    is_staff = models.BooleanField(default=False)  # REQUIRED for admin access
    is_superuser = models.BooleanField(default=False)  # REQUIRED for superusers
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
    contract_price = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    university = models.ForeignKey("api.University", on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'


class Sponsor(models.Model):
    class StatusChoices(models.TextChoices):
        NEW = 'new', 'New'
        IN_PROCESS = 'in_process', 'In process'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELLED = 'cancelled', 'Cancelled'

    class Amount_choice(models.TextChoices):
        MILLION = "1_000_000", "1 MLN UZS"
        FIVE_MILLION = "5_000_000", "5 MLN UZS"
        SEVEN_MILLION = "7_000_000", "7 MLN UZS"
        TEN_MILLION = "10_000_000", "10 MLN UZS"
        THIRTY_MILLION = "30_000_000", "30 MLN UZS"
        OTHERS = "OTHER", "OTHERS"

    class SponsorStatus(models.TextChoices):
        JURIDICAL = 'YURIDIK SHAXS', 'Yuridik shaxs'
        INDIVIDUAL = 'JISMONIY SHAXS', 'Jismoniy shaxs'

    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=30)
    amount = models.CharField(max_length=30, choices=Amount_choice.choices)
    custom_amount = models.CharField(max_length=50, blank=True, null=True)  # Custom amount for 'OTHERS'
    is_organization = models.BooleanField()
    progress = models.CharField(max_length=30, choices=StatusChoices.choices)
    sponsor_status = models.CharField(max_length=50, choices=SponsorStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    organization_name = models.CharField(max_length=250, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.sponsor_status = self.SponsorStatus.JURIDICAL if self.is_organization else self.SponsorStatus.INDIVIDUAL
        if not self.is_organization:
            self.organization_name = None

        # If 'OTHERS' is selected, validate and set custom_amount
        if self.amount == self.Amount_choice.OTHERS and not self.custom_amount:
            raise ValidationError({'custom_amount': "A custom amount must be provided when 'OTHERS' is selected!"})
        if self.amount != self.Amount_choice.OTHERS and self.custom_amount:
            self.custom_amount = None  # Reset custom amount if it's not needed

        super().save(*args, **kwargs)

    def clean(self):
        """Form yoki admin panel orqali validatsiya qo'shish."""
        if self.is_organization and not self.organization_name:
            raise ValidationError({'organization_name': "Yuridik shaxs uchun tashkilot nomi majburiy!"})
        if not self.is_organization and self.organization_name:
            raise ValidationError({'organization_name': "Jismoniy shaxs uchun tashkilot nomi kiritilmasligi kerak!"})

    def __str__(self):
        return f"{self.full_name} - {self.sponsor_status} - {self.amount}"

    class Meta:
        verbose_name = 'sponsor'
        verbose_name_plural = 'sponsors'


class StudentSponsor(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student, self.sponsor, self.amount, self.created_at

    class Meta:
        verbose_name = 'student sponsor'
        verbose_name_plural = 'student sponsors'
