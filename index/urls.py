from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'index'

urlpatterns = [
    path('', Index, name='index'), 
    #information machine type, model, site location, lastservice date(fk) running hour(fk) / 
    path('add_site/', add_site, name='add_site'),
    path('delete_site/<int:pk>', delete_site, name='delete_site'),
    path('modify_site/<int:pk>', modify_site, name='modify_site'),

 
]