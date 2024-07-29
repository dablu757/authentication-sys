from django.contrib import admin
from django.urls import path, include
from . views import *

urlpatterns = [
    path('regester/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name = 'login'),
]