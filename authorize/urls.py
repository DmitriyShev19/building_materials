from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
]

