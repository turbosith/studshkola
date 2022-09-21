from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput, ModelForm
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
    class Meta:
        model=Questions
        fields=['question','cat','photo']
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


