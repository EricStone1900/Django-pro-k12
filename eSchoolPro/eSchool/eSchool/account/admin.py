from django.contrib import admin
from .models import Profile, CustomUser
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo','interest']

@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
	list_display = ['username','nickname', 'gender','role']