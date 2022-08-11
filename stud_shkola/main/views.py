from django.shortcuts import render

# Create your views here.

from .models import questions
def menu(request):
    que=questions.objects.all()
    return render(request,'main/menu.html', {'title': 'StudШкола', 'que': que})
def mirea(request):
    return render(request,'main/mirea.html')