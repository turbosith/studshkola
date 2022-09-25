from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpResponseNotFound,Http404
# Create your views here.
from .forms import *
from .models import Questions, Category, Universities
from django.views.generic import ListView, CreateView


def menu(request):
    '''
    que = questions.object.order_by('-id')
    cats = Category.object.all()
    context={'title': 'StudШкола',
             'que': que,

             'cats': cats,
             'cat_selected': 0,
             }
    , context=context
    '''
    return render(request, 'main/index.html')
def mirea(request):
    return render(request,'main/university.html')

def certain_question(request,qid):
    return render(request,'main/askquestion.html', {'title': 'StudШкола'})
def universities(request, uid):
    return HttpResponse(f"<h1>ВУЗ: </h1><p>{uid}</p>")
def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена </h1><p>Что-то пошло не так:)")
'''
class MainQuestions(ListView):
    model=questions
    template_name = "main/questions.html"
    context_object_name = 'que'
    extra_context = {tit}
'''

def questions(request):
    que = Questions.objects.all()
    return render(request, 'main/questions.html', {'title': 'StudШкола', 'que': que})

def menuu(request):
    return render(request, 'main/menuu.html', {'title': 'Меню'})


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
def choice(request):

    if request.method== 'POST':
        form=Choise(request.POST,request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)

            return redirect('home')

    else:
        form=Choise()

    return render(request,'main/university.html', {'form':form, 'title': 'Выбрать ВУЗ'})
# class MainUniversity(ListView):
#     model=Questions
#     template_name = 'main/university.html'
#     context_object_name = 'univ'
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context= super().get_context_data(**kwargs)
#         context['title']='Выбор вуза'
#         return context
#     def get_queryset(self):
#         return Questions.objects.filter(is_published=True)


def show_uni(request):
    que = Questions.objects.order_by('-id')
    cats = Category.objects.all()
    uni = Category.objects.all()
    context = {'title': 'Вопросы',
               'que': que,
                'uni': uni,
               'cats': cats,
               'cat_selected': 0,
               }
    return render(request, 'main/university.html', context=context)

class MainCategory(ListView):
    model = Questions
    template_name = 'main/category.html'
    context_object_name = 'que'
    allow_empty = False

    def get_queryset(self):
        return Questions.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context
    #return HttpResponse(f"Отображение страницы {cat_id}")
def show_category(request):
     que = Questions.objects.order_by('-id')
     cats = Category.objects.all()
     context={'title': 'Вопросы',
              'que': que,

              'cats': cats,
              'cat_selected': 0,
              }
     return render(request, 'main/category.html',context=context)
def categories(request, cat_slug):
    cat=get_object_or_404(Category, slug=cat_slug)
    context={
        'cat':cat,
        'title':cat.name,
        #'cat_selected': university.name

    }
    return render(request, 'main/categories.html', context=context)

