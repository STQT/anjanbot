from django.urls import path
from app.address import views

urlpatterns = [
    path('', views.get_branches, name='branch_list'),
]
