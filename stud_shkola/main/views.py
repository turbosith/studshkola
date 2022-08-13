from django.shortcuts import render

# Create your views here.

from .models import questions
def menu(request):
    que=questions.objects.order_by('-id')
    return render(request,'main/index.html', {'title': 'StudШкола', 'que': que})
def mirea(request):
    return render(request,'main/mirea.html')
def askquestion(request):
    return render(request,'main/askquestion.html', {'title': 'StudШкола'})