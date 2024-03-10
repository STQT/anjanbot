from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ['name', 'is_active']


@admin.register(Product)
class ProductAdmin(TabbedTranslationAdmin):
    list_display = ['name', 'price', 'is_active']
    list_filter = ['category']
