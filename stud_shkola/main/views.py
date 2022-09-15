from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpResponseNotFound,Http404
# Create your views here.
from .forms import *
from .models import questions, Category, Universities


def menu(request):
    que = questions.objects.order_by('-id')
    cats = Category.objects.all()
    context={'title': 'StudШкола',
             'que': que,

             'cats': cats,
             'cat_selected': 0,
             }
    return render(request,'main/index.html', context=context)
def mirea(request):
    return render(request,'main/university.html')

def certain_question(request,qid):
    return render(request,'main/askquestion.html', {'title': 'StudШкола'})
def universities(request, uid):
    return HttpResponse(f"<h1>ВУЗ: </h1><p>{uid}</p>")
def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена </h1><p>Что-то пошло не так:)")
def questionss(request):
    que = questions.objects.all()
    return render(request, 'main/questions.html', {'title': 'StudШкола', 'que': que})
def menuu(request):
    return render(request, 'main/menuu.html', {'title': 'Меню'})
def show_category(request, cat_id):

    return HttpResponse(f"Отображение страницы {cat_id}")
def show_university(request, university_slug):
    university=get_object_or_404(Universities, slug=university_slug)
    context={
        'university':university,
        'title':university.name,
        #'cat_selected': university.name

    }
    return render(request, 'main/universities.html', context=context)

def askquestion(request):
    if request.method== 'POST':
        form=AddQuestionForm(request.POST,request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('home')

    else:
        form=AddQuestionForm()

    return render(request,'main/askquestion.html', {'form':form, 'title': 'Задать вопрос'})
#class RegisterUser(DataMixin, CreateView):
