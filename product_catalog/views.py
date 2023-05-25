"""
Модуль views.py в приложении product_catalog

Модуль views.py в приложении product_catalog определяет представления (views)
для обработки запросов, связанных с продуктами и категориями продуктов.

Зависимости:
- from django.shortcuts import render, redirect: для импорта функций `render`
и `redirect` Django.
- from django.views import View: для импорта класса `View` Django.
- from .models import Category, Product: для импорта моделей `Category` и
`Product` из модуля models.py.
- from .form import ProductForm: для импорта класса `ProductForm` из модуля
form.py.

Представления (views):
- product_card(request): представление для отображения страницы с информацией
о продукте.
- ProductByCategoryView(View): класс представления для отображения страницы с
продуктами определенной категории.
- ProductCreateView(View): класс представления для отображения страницы
создания нового продукта.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Category, Product, Cart, CartItem
from .form import ProductForm


def product_card(request):
    """
    Представление для отображения страницы с информацией о продукте.
    """
    return render(request, "product_catalog/product_card.html")


class ProductByCategoryView(View):
    """
    Класс представления для отображения страницы с продуктами определенной категории.
    """

    def get(self, request, category_id):
        """
        Обработчик GET-запроса.

        Получает идентификатор категории из URL-параметра.
        Извлекает категорию продуктов и список продуктов с этой категорией из
        базы данных.
        Формирует контекст с категорией и продуктами.
        Возвращает отрендеренный шаблон с переданным контекстом.
        """
        category = Category.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
        context = {"category": category, "products": products}
        return render(request, "product_catalog/product_by_category.html", context)


class ProductCreateView(View):
    """
    Класс представления для отображения страницы создания нового продукта.
    """

    def get(self, request):
        """
        Обработчик GET-запроса.

        Создает экземпляр формы для создания продукта.
        Формирует контекст с формой.
        Возвращает отрендеренный шаблон с переданным контекстом.
        """
        form = ProductForm()
        context = {"form": form}
        return render(request, "product_catalog/product_create.html", context)

    def post(self, request):
        """
        Обработчик POST-запроса.

        Создает экземпляр формы для создания продукта с переданными данными из
        запроса.
        Если форма действительна, сохраняет продукт и выполняет перенаправление
        на страницу с информацией о продукте.
        Если форма недействительна, формирует контекст с формой и возвращает
        отрендеренный шаблон с переданным контекстом.
        """
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_card")
        context = {"form": form}
        return render(request, "product_catalog/product_create.html", context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    cart, created = Cart.objects.get_or_create(user=user)

    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def view_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user).first()
    cart_items = CartItem.objects.filter(cart=cart)

    context = {
        'cart': cart,
        'cart_items': cart_items
    }

    return render(request, 'product_catalog/cart.html', context)