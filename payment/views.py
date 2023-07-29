from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
import os

from .crystalpay_sdk import CrystalPAY, InvoiceType
from product_catalog.views import count_price


crystalpayAPI = CrystalPAY(os.environ.get('AUTH_LOGIN'),
                           os.environ.get('SECRET1'),
                           os.environ.get('SECRET2')
                           )


class PayCartView(LoginRequiredMixin, View):
    login_url = 'account_login'

    def get(self, request, *args, **kwargs):
        dict_pay = crystalpayAPI.Invoice.create(count_price(request),
                                                          InvoiceType.purchase,
                                                          15)
        return redirect(dict_pay['url'])