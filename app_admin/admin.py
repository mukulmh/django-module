from django.contrib import admin
from .models import Product, Category, Manufacturer, Module, SubModule, Screen, UserRole, Rolewise_screen

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Module)
admin.site.register(SubModule)
admin.site.register(Screen)
admin.site.register(UserRole)
admin.site.register(Rolewise_screen)