from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Product
from .form import ProductForm


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


class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        context = {'form': form}
        return render(request, 'product_catalog/product_create.html', context)

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_card')
        context = {'form': form}
        return render(request, 'product_catalog/product_create.html', context)