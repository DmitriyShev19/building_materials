"""
Модуль models.py в приложении product_catalog

Модуль models.py в приложении product_catalog определяет модели Category и
Product, представляющие категории и продукты в каталоге продуктов.

Зависимости:
- from django.db import models: для импорта модуля `models` Django.

Модели:
- `Category`: модель, представляющая категорию продукта.
- `Product`: модель, представляющая продукт.

Атрибуты моделей:
- `short_name`: поле CharField, содержащее короткое название продукта.
- `full_name`: поле CharField, содержащее полное название продукта.
- `description`: поле TextField, содержащее описание продукта.
- `price`: поле DecimalField, содержащее цену продукта.
- `image`: поле ImageField, содержащее изображение продукта.
- `category`: поле ForeignKey, связанное с моделью `Category`, указывающее на
    категорию, к которой принадлежит продукт.
- `created_at`: поле DateTimeField, содержащее дату и время создания продукта.
- `updated_at`: поле DateTimeField, содержащее дату и время последнего
    обновления продукта.

Методы моделей:
- `__str__(self)`: метод, возвращающий строковое представление модели. В случае
модели `Category`, возвращает имя категории. В случае модели `Product`,
возвращает короткое название продукта.
"""

from django.db import models


class Category(models.Model):
    """
    Модель, представляющая категорию продукта.
    """

    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Модель, представляющая продукт.
    """

    short_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="construction_products/")
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_name
