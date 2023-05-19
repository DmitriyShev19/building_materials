from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from authorize.form import PersonForm
from authorize.models import Person


def index(request):
    return render(request, 'authorize/index.html')


@login_required
def profile(request):
    person = get_object_or_404(Person, pk=request.user.pk)
    return render(request, 'authorize/profile.html', {'person': person})


@login_required
def edit_person(request):
    person = Person.objects.get(pk=request.user.pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PersonForm(instance=person)

    return render(request, 'authorize/edit_person.html', {'form': form})
