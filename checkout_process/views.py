from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View


class CheckView(LoginRequiredMixin, View):
    login_url = 'account_login'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not (user.city and user.street and user.house_number and user.phone_numbers) :
            return redirect(reverse('edit_person'))
        return redirect(reverse('PayCart'))

