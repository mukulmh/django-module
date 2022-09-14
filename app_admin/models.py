from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    unit = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

# module, submodule & screen models
class Module(models.Model):
    module_name = models.CharField(max_length=200, unique=True)
    module_fa_icon = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.module_name

class SubModule(models.Model):
    sub_module_name = models.CharField(max_length=200, unique=True)
    sub_module_fa_icon = models.CharField(max_length=200)
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sub_module_name

class Screen(models.Model):
    screen_code = models.IntegerField(unique=True)
    screen_name = models.CharField(max_length=200, unique=True)
    screen_url = models.CharField(max_length=200, unique=True)
    screen_fa_icon = models.CharField(max_length=200, null=True)
    sub_module_id = models.ForeignKey(SubModule, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.screen_name

class UserRole(models.Model):
    role_name = models.CharField(max_length=200, unique=True)
    role_code = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role_name

class Rolewise_screen(models.Model):
    add = models.BooleanField()
    read = models.BooleanField()
    destroy = models.BooleanField()
    edit = models.BooleanField()
    role_id = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    screen_id = models.ForeignKey(Screen, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id