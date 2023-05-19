from django.contrib.auth.models import AbstractUser
from django.db import models


class Person(AbstractUser):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=20)
    phone_numbers = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d')


