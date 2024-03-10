from django.urls import path
from app.products import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.get_product, name='product_retrieve'),
]
