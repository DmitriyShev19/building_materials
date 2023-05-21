from django.shortcuts import render
from django.views import View
from .models import Category, Product

def product_card(request):
    return render(request, 'product_catalog/product_card.html')


class ProductByCategoryView(View):
    
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
        context = {
            'category': category,
            'products': products
        }
        return render(request, 'product_catalog/product_by_category.html',
                      context)