from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import Category, Product, Order


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ['name', 'is_active']


@admin.register(Product)
class ProductAdmin(TabbedTranslationAdmin):
    list_display = ['name', 'price', 'is_active']
    list_filter = ['category']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['filial', 'address', 'user_phone', 'all_cost', 'delivery']

    def user_phone(self, obj):
        return obj.user.phone if obj.user else None

    user_phone.short_description = 'Telefon raqam'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
