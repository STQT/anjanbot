# store/views.py
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.utils.translation import activate


def category_list(request):
    categories = Category.objects.all()
    language = request.GET.get('lang', 'uz')
    print(language)
    activate(language)
    return render(request, 'products/category_list.html', {'categories': categories})


def product_list(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    language = request.GET.get('lang', 'uz')
    activate(language)
    return render(request, 'products/product_list.html', {'category': category, 'products': products})


def get_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    language = request.GET.get('lang', 'uz')
    activate(language)
    data = {
        'id': product.pk,
        'price': product.price,
        'name': product.name,
        'image': product.image.url if product.image else '/static/images/not_found.jpeg',
        'count': 1
    }
    return JsonResponse(data)


def cart(request):
    # Retrieve cart data from session storage
    language = request.GET.get('lang', 'uz')
    activate(language)

    # Pass cart data to the template
    return render(request, 'products/cart.html')
