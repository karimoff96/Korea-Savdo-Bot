from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'created')


@admin.register(Elon)
class ElonAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'user', 'first_name', 'phone_number', 'address', 'model', 'created', 'active', 'price')


@admin.register(Mobil)
class MobilAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'user', 'first_name', 'phone_number', 'address', 'model', 'created', 'active', 'price')