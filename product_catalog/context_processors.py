"""
Модуль context_processors.py в приложении product_catalog

Модуль context_processors.py в приложении product_catalog определяет
контекстный процессор, который предоставляет категории продуктов в контексте
каждого запроса.

Зависимости:
- from .models import Category: для импорта модели `Category` из текущего
пакета.

Контекстный процессор:
- `categories(request)`: функция контекстного процессора, которая получает все
категории продуктов и возвращает их в виде словаря в контексте запроса.
"""
from .models import Category


def categories(request):
    """
    Контекстный процессор, предоставляющий категории продуктов в контексте
    каждого запроса.

    :param request: объект запроса
    :return: словарь с категориями продуктов в контексте
    """
    categories = Category.objects.all()
    return {"categories": categories}
