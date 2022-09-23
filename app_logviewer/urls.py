from django.urls import path
from .views import *

urlpatterns = [
    path('logs/', logs, name='logs'),
]