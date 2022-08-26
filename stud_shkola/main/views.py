from django.shortcuts import render,HttpResponse, redirect
from django.http import HttpResponseNotFound,Http404
# Create your views here.

from .models import questions
def menu(request):
    que=questions.objects.order_by('-id')
    return render(request,'main/index.html', {'title': 'StudШкола', 'que': que})
def mirea(request):
    return render(request,'main/mirea.html')
def askquestion(request):
    return render(request,'main/askquestion.html', {'title': 'StudШкола'})
def certain_question(request,qid):
    return render(request,'main/askquestion.html', {'title': 'StudШкола'})
def universities(request, uid):
    return HttpResponse(f"<h1>ВУЗ: </h1><p>{uid}</p>")
def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена </h1><p>Что-то пошло не так:)")
def questionss(request):
    que = questions.objects.all()
    return render(request, 'main/questions.html', {'title': 'StudШкола', 'que': que})