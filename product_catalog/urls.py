"""
Модуль urls.py в приложении product_catalog

Модуль urls.py в приложении product_catalog определяет маршруты URL для
обработки запросов, связанных с продуктами и категориями продуктов.

Зависимости:
- from django.urls import path: для импорта функции `path` Django.
- from .views import *: для импорта всех представлений (views) из модуля
views.py приложения product_catalog.

Маршруты URL:
- '/product_card/': URL для отображения страницы с информацией о продукте.
Связанное представление: `product_card`. Имя маршрута: 'product_card'.
- '/category/<int:category_id>/': URL для отображения страницы с продуктами
определенной категории. Связанное представление: `ProductByCategoryView`.
Имя маршрута: 'product_by_category'.
- '/product/create/': URL для отображения страницы создания нового продукта.
Связанное представление: `ProductCreateView`. Имя маршрута: 'product_create'.
"""
from django.urls import path
from .views import *

urlpatterns = [
    path("product_card/", product_card, name="product_card"),
    path(
        "category/<int:category_id>/",
        ProductByCategoryView.as_view(),
        name="product_by_category",
    ),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
]
