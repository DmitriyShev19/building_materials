"""
Модуль admin.py в приложении product_catalog

Модуль admin.py в приложении product_catalog позволяет настроить
административный интерфейс Django для работы с моделями Category и Product.

Зависимости:
- from django.contrib import admin: для импорта модуля `admin` Django.
- from .models import Category, Product: для импорта моделей `Category` и
`Product` из текущего пакета.

Регистрация моделей:
- `admin.site.register(Category)`: регистрирует модель `Category` в
административном интерфейсе Django, что позволяет администратору управлять
данными этой модели через интерфейс администратора.
- `admin.site.register(Product)`: регистрирует модель `Product` в
административном интерфейсе Django, что позволяет администратору управлять
данными этой модели через интерфейс администратора.

Пример использования:
from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
"""
from django.contrib import admin

from .models import Category, Product

admin.site.register(Category)
