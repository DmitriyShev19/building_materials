"""
Модуль urls.py в приложении authorize

Модуль urls.py в приложении authorize определяет маршруты URL (URL patterns),
которые будут использоваться в приложении.

Зависимости:
- from django.urls import path: для импорта функции `path` для определения пути
URL.
- from django.views.decorators.cache import cache_page: для импорта функции
`cache_page`, если требуется кэширование представлений.
- from .views import *: для импорта всех представлений (views) из модуля views.py.

URL patterns:
- Пустой путь URL (''): соответствует функции `index` из модуля views.py и
имеет имя 'index'.
- Путь URL 'profile/': соответствует функции `profile` из модуля views.py и
имеет имя 'profile'.
- Путь URL 'edit_person/': соответствует функции `edit_person` из модуля
views.py и имеет имя 'edit_person'.

"""
from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("profile/", profile, name="profile"),
    path("edit_person/", edit_person, name="edit_person"),
]
