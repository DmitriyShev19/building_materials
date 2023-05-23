"""
Модуль authorize

Модуль `authorize` содержит представления и модели, связанные с аутентификацией
и профилем пользователя.
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from authorize.forms import PersonForm
from authorize.models import Person


def index(request):
    """
    Отображает главную страницу.

    Аргументы:
    - request: объект запроса Django.

    Возвращает:
    - Отрисованный шаблон 'authorize/index.html'.

    Зависимости:
    - from django.shortcuts import render
    """
    return render(request, "authorize/index.html")


@login_required
def profile(request):
    """
    Отображает профиль пользователя.

    Аргументы:
    - request: объект запроса Django.

    Возвращает:
    - Отрисованный шаблон 'authorize/profile.html' с информацией о пользователе.

    Зависимости:
    - from django.contrib.auth.decorators import login_required
    - from django.shortcuts import render, get_object_or_404
    - from authorize.models import Person
    """
    person = get_object_or_404(Person, pk=request.user.pk)
    return render(request, "authorize/profile.html", {"person": person})


@login_required
def edit_person(request):
    """
    Позволяет пользователю редактировать свой профиль.

    Аргументы:
    - request: объект запроса Django.

    Возвращает:
    - Отрисованный шаблон 'authorize/edit_person.html' с формой редактирования профиля.

    Зависимости:
    - from django.contrib.auth.decorators import login_required
    - from django.shortcuts import render, redirect, get_object_or_404
    - from authorize.form import PersonForm
    - from authorize.models import Person
    """
    person = Person.objects.get(pk=request.user.pk)
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = PersonForm(instance=person)

    return render(request, "authorize/edit_person.html", {"form": form})
