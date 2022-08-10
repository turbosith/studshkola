from django.shortcuts import render

# Create your views here.

from .models import questions
def menu(request):
    gue=questions.objects.all()
    return render(request,'main/menu.html', {'title': 'Главная страница', 'que': questions})
def mirea(request):
    return render(request,'main/mirea.html')