
from django.urls import path
from .views import register_user, user_login,create_product,retrieve_product

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('products/create/', create_product, name='create-product'),
    path('products/<int:pk>/', retrieve_product, name='retrieve-product'),
]