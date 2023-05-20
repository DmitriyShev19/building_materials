from django.shortcuts import render


def product_card(request):
    return render(request, 'product_catalog/product_card.html')
