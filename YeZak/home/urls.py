from django.urls import path
from .views import *

urlpatterns = [
    path('', web, name='web'),
]