from django.urls import path

from .views import edit_category, edit_manufacturer, edit_product, profile, product, manufacturer, category, delete_product, delete_category, delete_manufacturer

urlpatterns =[
    path('profile/', profile, name='profile'),
    path('products/', product, name='products'),
    path('delete-product/<int:id>', delete_product, name='delete-product'),
    path('edit-product/<int:id>', edit_product, name='edit-product'),
    path('categories/', category, name='categories'),
    path('edit-category/<int:id>', edit_category, name='edit-category'),
    path('delete-category/<int:id>', delete_category, name='delete-category'),
    path('manufacturers/', manufacturer, name='manufacturers'),
    path('delete-manufacturer/<int:id>', delete_manufacturer, name='delete-manufacturer'),
    path('edit-manufacturer/<int:id>', edit_manufacturer, name='edit-manufacturer'),
]