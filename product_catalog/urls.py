from django.urls import path
from .views import *

urlpatterns = [
    path('product_card/', product_card, name='product_card'),
    path('category/<int:category_id>/', ProductByCategoryView.as_view(),
         name='product_by_category'),
    path('product/create/', ProductCreateView.as_view(),
         name='product_create'),
]