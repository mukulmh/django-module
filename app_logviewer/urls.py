from django.urls import path
from .views import *

urlpatterns = [
    path('', logs, name='logs'),
]