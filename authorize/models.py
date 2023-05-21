"""
Модуль models.py в приложении authorize

Модуль models.py в приложении authorize содержит определение модели `Person`,
которая является наследником `AbstractUser` из модуля
`django.contrib.auth.models`.

Зависимости:
- from django.contrib.auth.models import AbstractUser: для импорта базового
класса `AbstractUser`.
- from django.db import models: для импорта модуля `models` Django.

Класс Person:
- Наследуется от `AbstractUser`, что позволяет использовать стандартные поля и
функциональность, предоставляемые Django для модели пользователя.
- Содержит дополнительные пользовательские поля:
    - city: поле CharField для хранения названия города пользователя
    (максимальная длина 100 символов).
    - street: поле CharField для хранения названия улицы пользователя
    (максимальная длина 100 символов).
    - house_number: поле CharField для хранения номера дома пользователя
    (максимальная длина 20 символов).
    - phone_numbers: поле CharField для хранения номера телефона пользователя
    (максимальная длина 20 символов).
    - avatar: поле ImageField для загрузки и хранения аватара пользователя.
    Аватары сохраняются в папке 'photos/%Y/%m/%d'.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class Person(AbstractUser):
    city = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=100, null=True)
    house_number = models.CharField(max_length=20, null=True)
    phone_numbers = models.CharField(max_length=20, null=True)
    avatar = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
