from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import TextInput, ModelForm, Textarea
from .models import *


class AddQuestionForm(forms.ModelForm):
    '''
    question = forms.CharField(widget=forms.Textarea(attrs={'cols':40, 'rows':2}),label="Вопрос*")
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория*", empty_label="Категория не выбрана")
    photo = forms.ImageField(required=False, label="Фотография")
    '''
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label="Категория не выбрана"
        self.fields['uni'].empty_label = "Из какого вы ВУЗа?/По какому ВУЗу у вас вопрос?"
    class Meta:
        model=Questions
        fields=['question','cat','uni','photo']
        widgets={
            'question':forms.Textarea(attrs={'cols':40, 'rows':2})
        }

    def clean_title(self):
        question=self.cleaned_data['question']
        if len(question)>255:
            raise ValidationError('Длинна превышает 255 символов')
        return question


class Choise(forms.ModelForm):
    '''
    question = forms.CharField(widget=forms.Textarea(attrs={'cols':40, 'rows':2}),label="Вопрос*")
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория*", empty_label="Категория не выбрана")
    photo = forms.ImageField(required=False, label="Фотография")
    '''
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['uni'].empty_label="Категория не выбрана"
    class Meta:
        model=Questions
        fields=['uni']
        widgets={
            'question':forms.Textarea(attrs={'cols':40, 'rows':2})
        }
    def clean_title(self):
        question=self.cleaned_data['uni']

        return question
class RegisterUserForm(UserCreationForm):
    username= forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email=forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    phone= forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-input'}))
    level=forms.ModelChoiceField(label='Уровень образования',queryset=LevelEducation.objects.all(), empty_label='Уровень образования')
    password1= forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2= forms.CharField(label='Повтор пароля',widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model=User
        fields=('username','email','phone','password1','password2')
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=('text',)
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
        self.fields['text'].widget=Textarea(attrs={'rows':5})
