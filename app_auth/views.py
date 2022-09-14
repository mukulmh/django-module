from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth, messages
from django.core import serializers
from django.http import JsonResponse

from .models import Account
from app_admin.models import *

# Create your views here.

# login
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            userrole = Account.objects.get(email=email)
            rolewiseScreen = Rolewise_screen.objects.filter(role_id = userrole.user_role_id)
            screensID = []
            for screen in rolewiseScreen:
                screensID.append(screen.screen_id_id)
            request.session['userscreens'] = screensID

            moduleData = []

            modules = Module.objects.all()
            for module in modules:
                moduleJson = {}
                moduleJson['module_id'] = module.id
                moduleJson['module_name'] = module.module_name
                moduleJson['icon'] = module.module_fa_icon
    
                subModuleData = []
                submodules = SubModule.objects.filter(module_id = module.id)
                for submodule in submodules:
                    subModuleJson = {}
                    subModuleJson['sub_module_id'] = submodule.id
                    subModuleJson['sub_module_name'] = submodule.sub_module_name
                    subModuleJson['icon'] = submodule.sub_module_fa_icon

                    screenData = []
                    screens = Screen.objects.filter(sub_module_id = submodule.id)
                    for screen in screens:
                        screenJson = {}
                        screenJson['screen_id'] = screen.id
                        screenJson['screen_name'] = screen.screen_name
                        screenJson['screen_url'] = screen.screen_url
                        screenJson['icon'] = screen.screen_fa_icon
                        screenJson['code'] = screen.screen_code
                        screenData.append(screenJson)
                    
                    subModuleJson['screens'] = screenData
                    subModuleData.append(subModuleJson)

                moduleJson['sub_modules'] = subModuleData
                moduleData.append(moduleJson)

            request.session['modules'] = moduleData

            auth.login(request,user) 
            # return JsonResponse(moduleData, safe=False) 
            return redirect('profile')

        else:
            messages.info(request, 'Invalid email or password!')

    return render(request, 'auth/login-v2.html')


# register
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if Account.objects.filter(username=username):
                messages.info(request,'Username is already takes!')
            elif Account.objects.filter(email=email):
                messages.info(request, 'Email is already been taken!')
            else:
                user = Account.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.info(request, 'User registration successfull.')
                return redirect('login')
        else:
            messages.info(request, 'Password did not matched!')
    return render(request, 'auth/register-v2.html')


# forgot password
def forgot_password(request):
    return render(request, 'auth/forgot-password-v2.html')


# recover password
def recover_password(request):
    return render(request, 'auth/recover-password-v2.html')

# sign out
def sign_out(request):
    auth.logout(request)
    return redirect('login')
