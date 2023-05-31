from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('category/<int:category_id>/', topic_list, name='topic_list'),
    path('topic/<int:topic_id>/', topic_detail, name='topic_detail'),
]