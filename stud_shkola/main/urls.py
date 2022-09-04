from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import show_category

urlpatterns = [
    path('', views.menu, name='home'),
    path('mirea', views.mirea, name='mirea'),
    path('askquestion', views.askquestion, name='askquestion'),
    path('certain_question/<int:qid>/', views.certain_question, name='certain_question'),
    path('universities/<slug:uid>/',views.universities),
    path('questions', views.questionss, name='questions'),
    path('category/<int:cat_id>/', show_category, name='category'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

