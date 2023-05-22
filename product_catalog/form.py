"""
Модуль forms.py в приложении product_catalog

Модуль forms.py в приложении product_catalog определяет форму ProductForm для
создания и обновления объектов модели Product.

Зависимости:
- from django import forms: для импорта модуля `forms` Django.
- from .models import Product: для импорта модели `Product` из текущего пакета.

Класс формы:
- `ProductForm`: класс формы, основанный на модели `Product`, используемый для
создания и обновления объектов модели `Product`.

Атрибуты класса:
- `model = Product`: указывает, что форма основана на модели `Product`.
- `fields`: перечисляет поля модели `Product`, которые должны присутствовать в
форме.

"""
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """
    Форма для создания и обновления объектов модели Product.
    """

    class Meta:
        model = Product
        fields = (
            "short_name",
            "full_name",
            "description",
            "price",
            "image",
            "category",
        )
