from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpResponseNotFound,Http404
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin

from .forms import *
from .models import Questions, Category, Universities
from django.views.generic import ListView, CreateView, DetailView
from .utils import *
from django.contrib import messages
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
'''
def certain_question(request,qid):
    que = Questions.objects.get(pk=qid)
    context = {
        'que': que,
        'title': que.question,
        # 'cat_selected': university.name

    }
    return render(request, 'main/certain_question.html', context=context)
'''


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)
class CertainQuestion(CustomSuccessMessageMixin,FormMixin, DetailView):
    model=Questions
    template_name = 'main/certain_question.html'
    context_object_name = 'que'
    form_class=CommentForm
    success_msg = 'Ответ успешно создан'
    #def get_queryset(self):
        #return Questions.objects.get(pk=self.kwargs['qid'])
    def get_success_url(self):
        return reverse_lazy('certain_question', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.quest = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)




def universities(request, uid):
    return HttpResponse(f"<h1>ВУЗ: </h1><p>{uid}</p>")
def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена </h1><p>Что-то пошло не так:)")
'''
class MainQuestions(ListView):
    model=questions
    template_name = "main/certain_question.html"
    context_object_name = 'que'
    extra_context = {tit}
'''

def questions(request):
    que = Questions.objects.all()
    return render(request, 'main/certain_question.html', {'title': 'StudШкола', 'que': que})

def menuu(request):
    return render(request, 'main/menuu.html', {'title': 'Меню'})


def show_university(request, university_slug):
    university=get_object_or_404(Universities, slug=university_slug)
    que = Questions.objects.filter(uni__name=university.name)
    context={
        'university':university,
        'title':university.name,
        'que':que,
        #'cat_selected': university.name

    }
    return render(request, 'main/universities.html', context=context)

'''
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
    '''
class AsKQuestion(LoginRequiredMixin, DataMixin,CreateView):
    login_url=reverse_lazy('login')
    model=Questions
    template_name = 'main/askquestion.html'
    form_class = AddQuestionForm
    success_url = reverse_lazy('category')
    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.author=self.request.user
        self.object.save()
        return super().form_valid(form)


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
    uni = Universities.objects.order_by('-name')
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
    cats = Category.objects.all()
    catt=get_object_or_404(Category, slug=cat_slug)

    que = Questions.objects.filter(cat__slug=catt.slug)
    context = {
        'cats': cats,
        'cat': catt,
        'title': catt.name,
        'que': que,
        # 'cat_selected': university.name

    }
    return render(request, 'main/categories.html', context=context)
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')
    success_msg='Вы успешно зарегистрировались'
    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title="Регистрация")
        return dict(list(context.items())+list(c_def.items()))
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title="Авторизация")
        return dict(list(context.items())+list(c_def.items()))
    def get_success_url(self):
        return reverse_lazy('home')
def logout_user(request):
    logout(request)
    return redirect('login')
class Profile(LoginRequiredMixin, ListView):
    login_url = 'login'
    model=Questions
    template_name = 'main/profile.html'
    context_object_name = 'que'
    form_class=CommentForm
    def get_queryset(self):

        return Questions.objects.all()



