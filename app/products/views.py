# store/views.py
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})


def product_list(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products/product_list.html', {'category': category, 'products': products})


def get_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    data = {
        'price': product.price,
        'name': product.name,
        'image': product.image.url if product.image else None,
        'count': 1
    }
    return JsonResponse(data)
