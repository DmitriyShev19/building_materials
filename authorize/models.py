from django.contrib.auth.models import AbstractUser
from django.db import models


class Person(AbstractUser):
    city = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=100, null=True)
    house_number = models.CharField(max_length=20, null=True)
    phone_numbers = models.CharField(max_length=20, null=True)
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)


