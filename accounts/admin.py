from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ("email", "is_staff", "is_active", "verification_code")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(User, CustomUserAdmin)

