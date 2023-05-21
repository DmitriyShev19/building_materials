"""
Модуль admin.py в приложении authorize

Модуль admin.py в приложении authorize содержит настройки административного
интерфейса Django для модели Person.
"""

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Person

admin.site.register(Person, UserAdmin)
