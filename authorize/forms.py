"""
Модуль forms.py в приложении authorize

Модуль forms.py в приложении authorize содержит определение формы `PersonForm`
для модели `Person`.

Зависимости:
- from django import forms: для импорта модуля форм Django.
- from .models import Person: для импорта модели `Person`, которая будет
использоваться в форме.

Класс PersonForm:
- Наследуется от `forms.ModelForm`, предоставляющего возможность создания формы
 на основе модели.
- Использует метакласс `Meta` для определения свойств модели, которые будут
использованы в форме.

Свойства класса Meta:
- model: модель, с которой будет связана форма (Person).
- fields: список полей модели, которые будут отображаться в форме.

Пример использования формы:
form = PersonForm(request.POST, request.FILES, instance=person)
form.is_valid()  # Проверка валидности формы
form.save()  # Сохранение данных из формы в модель
"""
from django import forms
from .models import Person
from allauth.account.forms import LoginForm, SignupForm


class PersonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].label = "Аватар"
        #и так далее создаём поля, которые будут отображаться
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Person
        fields = [
            "avatar",
            "first_name",
            "last_name",
            "email",
            "phone_numbers",
            "city",
            "street",
            "house_number",
        ]