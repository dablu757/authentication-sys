from django.contrib import admin
from django.urls import path, include
from . views import *

urlpatterns = [
    path('regester/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('profile/', UserProfileView.as_view(), name = 'profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name = 'changepassword'),
    path('send-reset-passwprd-email/', SendPasswordResetEmailView.as_view(), name = 'send-reset-passwprd-email'),
]