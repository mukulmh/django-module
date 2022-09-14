from django.urls import path
from .views import login,register,forgot_password,recover_password, sign_out


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', sign_out, name='logout'),
    path('register/', register, name='register'),
    path('forgot-password/', forgot_password, name='forgot-password'),
    path('recover-password/', recover_password, name='recover-password'),
]