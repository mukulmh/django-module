from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

# Create your views here.

# profile
def profile(request):
    if request.user.is_authenticated:
        userscreens = request.session['userscreens']
        modules = request.session['modules']
        return render(request, 'adminlte/profile.html', {'modules': modules, 'userscreens': userscreens})
    return redirect('login')

# product
def product(request):
    if request.user.is_authenticated:
        userscreens = request.session['userscreens']
        modules = request.session['modules']
        products = Product.objects.all()
        categories = Category.objects.all()
        manufacturers = Manufacturer.objects.all()
        if request.method == 'POST':
            name = request.POST['name']
            category = request.POST['category']
            manufacturer = request.POST['manufacturer']
            unit = request.POST['unit']
            price = request.POST['price']

            if Product.objects.filter(name=name).exists():
                messages.info(request, 'This product is already added.')
            else:
                product = Product(name=name, category_id=category, manufacturer_id=manufacturer, unit=unit, price=price)
                product.save()
            return redirect('products')

        return render(request, 'adminlte/product.html', {'modules': modules,'products': products, 'categories': categories, 'manufacturers': manufacturers, 'userscreens': userscreens})
    return redirect('login')


# edit product
def edit_product(request, id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        product.name = request.POST['name']
        product.category_id = request.POST['category']
        product.manufacturer_id = request.POST['manufacturer']
        product.unit = request.POST['unit']
        product.price = request.POST['price']
        product.save()
        return redirect('products')
    return redirect('login')


# delete product
def delete_product(request, id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('products')
    return redirect('login')


# category
def category(request):
    if request.user.is_authenticated:
        userscreens = request.session['userscreens']
        modules = request.session['modules']
        categories = Category.objects.all()
        if request.method == 'POST':
            name = request.POST['name']
            if Category.objects.filter(name=name).exists():
                messages.info(request, 'This category is already added!')
            else:
                category = Category(name=name)
                category.save()
            return redirect('categories')
        return render(request, 'adminlte/category.html',{'categories': categories, 'modules':modules, 'userscreens':userscreens})
    return redirect('login')


# edit category
def edit_category(request, id):
    if request.user.is_authenticated:
        category = Category.objects.get(id=id)
        category.name = request.POST['name']
        category.save()
        return redirect('categories')
    return redirect('login')


# delete category
def delete_category(request, id):
    if request.user.is_authenticated:
        category = Category.objects.get(id=id)
        category.delete()
        return redirect('categories')
    return redirect('login')


# manufacturer
def manufacturer(request):
    if request.user.is_authenticated:
        userscreens = request.session['userscreens']
        modules = request.session['modules']
        manufacturers = Manufacturer.objects.all()
        if request.method == 'POST':
            name = request.POST['name']
            if Manufacturer.objects.filter(name=name).exists():
                messages.info(request, 'Manufacturer already exists!')
            else:
                manufacturer = Manufacturer(name=name)
                manufacturer.save()
            return redirect('manufacturers')
        return render(request, 'adminlte/manufacturer.html',{'manufacturers': manufacturers, 'modules':modules, 'userscreens':userscreens})
    return redirect('login')


# edit manufacturer
def edit_manufacturer(request, id):
    if request.user.is_authenticated:
        manufacturer = Manufacturer.objects.get(id=id)
        manufacturer.name = request.POST['name']
        manufacturer.save()
        return redirect('manufacturers')
    return redirect('login')


# delete manufacturer
def delete_manufacturer(request, id):
    if request.user.is_authenticated:
        manufacturer = Manufacturer.objects.get(id=id)
        manufacturer.delete()
        return redirect('manufacturers')
    return redirect('login')