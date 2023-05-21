from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('short_name', 'full_name', 'description',
                  'price', 'image', 'category')
