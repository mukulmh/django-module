from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

# Create your views here.

# profile
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST['name']
            username = request.POST['username']
            email = request.POST['email']
            user = request.user
            user.name = name
            user.username = username
            user.email = email
            user.save()
            messages.success(request, 'User info updated!')
        userscreens = request.session['userscreens']
        modules = request.session['modules']
        role = request.user.user_role_id.id
        return render(request, 'adminlte/profile.html', {'modules': modules, 'userscreens': userscreens, 'role': role})
    messages.error(request,'Please sign in first!')
    return redirect('login')

# product
def product(request):
    if request.user.is_authenticated:
        userscreens = request.session['userscreens']
        modules = request.session['modules']
        products = Product.objects.all()
        categories = Category.objects.all()
        manufacturers = Manufacturer.objects.all()
        
        role = request.user.user_role_id.id

        if request.method == 'POST':
            name = request.POST['name']
            category = request.POST['category']
            manufacturer = request.POST['manufacturer']
            unit = request.POST['unit']
            price = request.POST['price']

            if Product.objects.filter(name=name).exists():
                messages.error(request, 'This product is already added.')
            else:
                product = Product(name=name, category_id=category, manufacturer_id=manufacturer, unit=unit, price=price)
                product.save()
                messages.success(request, 'Product added!')
            return redirect('products')

        return render(request, 'adminlte/product.html', {'modules': modules,'products': products, 'categories': categories, 'manufacturers': manufacturers, 'userscreens': userscreens, 'sideScreen': 'All Products', 'sideSub': 'Product', 'sideModule': 'Products', 'role': role})
    messages.error(request,'Please sign in first!')
    return redirect('login')


# edit product
def edit_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id = request.POST['id']
            product = Product.objects.get(id=id)
            product.name = request.POST['name']
            product.category_id = request.POST['category']
            product.manufacturer_id = request.POST['manufacturer']
            product.unit = request.POST['unit']
            product.price = request.POST['price']
            product.save()
            messages.success(request,'Product updated!')
        return redirect('products')
    messages.error(request,'Please sign in first!')
    return redirect('login')


# delete product
def delete_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id = request.POST['id']
            product = Product.objects.get(id=id) 
            product.delete()
            messages.success(request, 'Product deleted!')
        return redirect('products')
    return redirect('login')


# category
def category(request):
    if request.user.is_authenticated:
        userscreens = request.session['userscreens']
        modules = request.session['modules']
        categories = Category.objects.all()
        
        role = request.user.user_role_id.id

        if request.method == 'POST':
            name = request.POST['name']
            if Category.objects.filter(name=name).exists():
                messages.error(request, 'This category is already added!')
            else:
                category = Category(name=name)
                category.save()
                messages.success(request, 'Category added!')
            return redirect('categories')
        return render(request, 'adminlte/category.html',{'categories': categories, 'modules':modules, 'userscreens':userscreens , 'sideScreen': 'Category', 'role': role})
    return redirect('login')


# edit category
def edit_category(request):
    if request.user.is_authenticated:
        id = request.POST['id']
        category = Category.objects.get(id=id)
        category.name = request.POST['name']
        category.save()
        messages.success(request, 'Category updated!')
        return redirect('categories')
    return redirect('login')


# delete category
def delete_category(request):
    if request.user.is_authenticated:
        id = request.POST['id']
        category = Category.objects.get(id=id)
        category.delete()
        messages.success(request, 'Category deleted!')
        return redirect('categories')
    return redirect('login')


# manufacturer
def manufacturer(request):
    if request.user.is_authenticated:
        userscreens = request.session['userscreens']
        modules = request.session['modules']
        manufacturers = Manufacturer.objects.all()

        role = request.user.user_role_id.id

        if request.method == 'POST':
            name = request.POST['name']
            if Manufacturer.objects.filter(name=name).exists():
                messages.error(request, 'Manufacturer already exists!')
            else:
                manufacturer = Manufacturer(name=name)
                manufacturer.save()
                messages.success(request, 'Manufacturer added!')
            return redirect('manufacturers')
        return render(request, 'adminlte/manufacturer.html',{'manufacturers': manufacturers, 'modules':modules, 'userscreens':userscreens, 'sideScreen': 'All Manufacturers', 'sideSub': 'Manufacturer', 'sideModule': 'Products', 'role': role})
    messages.error(request,'Please sign in first!')
    return redirect('login')


# edit manufacturer
def edit_manufacturer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id = request.POST['id']
            manufacturer = Manufacturer.objects.get(id=id)
            manufacturer.name = request.POST['name']
            manufacturer.save()
            messages.success(request, 'Manufacturer updated!')
        return redirect('manufacturers')
    return redirect('login')


# delete manufacturer
def delete_manufacturer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id = request.POST['id']
            manufacturer = Manufacturer.objects.get(id=id)
            manufacturer.delete()
            messages.success(request, 'Manufacturer deleted!')
        return redirect('manufacturers')
    return redirect('login')