from django.urls import path

from .views import *

urlpatterns = [
    path('', PayCartView.as_view(), name='PayCart'),
]