from django.urls import path

from .views import *

urlpatterns =[
    path('', profile, name='profile'),
    path('products/', product, name='products'),
    path('delete-product/', delete_product, name='delete-product'),
    path('edit-product/', edit_product, name='edit-product'),
    path('categories/', category, name='categories'),
    path('edit-category/', edit_category, name='edit-category'),
    path('delete-category/', delete_category, name='delete-category'),
    path('manufacturers/', manufacturer, name='manufacturers'),
    path('delete-manufacturer/', delete_manufacturer, name='delete-manufacturer'),
    path('edit-manufacturer/', edit_manufacturer, name='edit-manufacturer'),
    path('users/', users, name='users'),
]