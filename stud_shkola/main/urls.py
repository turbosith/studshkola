from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import MainUniversity, MainCategory

urlpatterns = [
    path('', views.menu, name='home'),
    path('mirea', views.mirea, name='mirea'),
    path('askquestion', views.askquestion, name='askquestion'),
    path('certain_question/<int:qid>/', views.certain_question, name='certain_question'),

    path('questions', views.questions, name='questions'),

    path('menuu', views.menuu, name='menuu'),
    #path('register', RegisterUser.as_view(), name='register'),
    #path('login', views.login, name='login'),
    path('university', views.show_uni, name='university'),
    path('universities/<slug:university_slug>/', views.show_university, name='universities'),
    path('category', views.show_category, name='category'),
    path('categories/<slug:cat_slug>/', views.categories, name='categories'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

