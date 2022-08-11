from django.shortcuts import render
from django.urls import path
from . import views
urlpatterns = [
    path('', views.menu, name='home'),
    path('mirea', views.mirea, name='mirea'),
    path('askquestion', views.askquestion, name='askquestion')
]
