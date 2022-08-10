from django.shortcuts import render
from django.urls import path
from . import views
urlpatterns = [
    path('', views.menu, name='home'),
    path('mirea', views.mirea, name='mirea')
]
