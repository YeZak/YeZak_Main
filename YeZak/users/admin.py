import email
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     on_delete = False

# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline,)

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
# admin.site.register(Profile)
