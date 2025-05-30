from django.urls import path

from . import views

urlpatterns = [
path("products/", views.product_list, name="product_list"),
path('products/create/', views.product_create, name='product_create'),
path('products/<int:pk>/', views.product_detail, name='product_detail'),
path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
path("products/<int:pk>/delete/", views.product_soft_delete, name="product_delete"),

]