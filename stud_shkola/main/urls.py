from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import MainCategory, RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('', views.menu, name='home'),
    path('mirea', views.mirea, name='mirea'),
    path('askquestion', views.askquestion, name='askquestion'),
    path('certain_question/<int:qid>/', views.certain_question, name='certain_question'),



    path('menuu', views.menuu, name='menuu'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('university', views.show_uni, name='university'),
    path('universities/<slug:university_slug>/', views.show_university, name='universities'),
    path('category', views.show_category, name='category'),
    path('categories/<slug:cat_slug>/', views.categories, name='categories'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

