from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username')
@admin.register(Elon)
class ElonAdmin(admin.ModelAdmin):
    list_display = ('elon_id', 'first_name', 'category', 'phone_number', 'address', 'model', 'cr_on', 'price')