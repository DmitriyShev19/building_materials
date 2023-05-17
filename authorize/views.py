from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'authorize/index.html')


@login_required
def profile(request):
    return render(request, 'authorize/profile.html')