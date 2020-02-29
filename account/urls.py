from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'account'

urlpatterns = [
    path('Login', Login, name='Login'),
    path('Logout', Logout, name='Logout'),
    path('Signup', Signup, name='Signup'),
]

