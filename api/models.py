from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from api.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('student', 'Student'),
        ('admin', 'Administrator'),
        ('sponsor', 'Sponsor'),
    ]

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='user')
    avatar = models.ImageField(upload_to="avatar/student", default="./student.webp")
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email, self.role, self.first_name, self.last_name