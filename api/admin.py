from django.contrib import admin
from django.utils.html import format_html
from .models import (
    User,
    Student,
    Sponsor,
    StudentSponsor,
    University
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'role', 'image_tag')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    list_per_page = 8

    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.avatar.url}" target="_blank"><img src="{obj.avatar.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 8

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'degree', 'allocated_money', 'contract_price', 'university')
    search_fields = ('full_name', 'degree')
    list_per_page = 8

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'deposit_money', 'is_organization','progress','sponsor_status', 'created_at', 'organization_name', 'spent_amount')
    search_fields = ('full_name', 'phone_number', 'organization_name')
    list_per_page = 8

@admin.register(StudentSponsor)
class StudentSponsorAdmin(admin.ModelAdmin):
    list_display = ('student', 'sponsor', 'amount', 'created_at')
    search_fields = ('student', 'sponsor')
    list_per_page = 8