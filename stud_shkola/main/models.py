from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

categ={}
class Questions(models.Model):
    cat = models.ForeignKey('Category',on_delete=models.PROTECT, null=True, verbose_name="Категория")
    question=models.TextField( blank=True, verbose_name="Вопрос")
    photo=models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фотография",blank=True)
    uni = models.ForeignKey('Universities', on_delete=models.PROTECT, blank=True, verbose_name="Вузы", null=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор вопроса", blank=True, null=True)
    time_create=models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True, verbose_name="Опубликовано")


    def __str__(self):
        return self.question
    def get_absolute_url(self):
        return reverse('certain_question', kwargs={'qid':self.pk})
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering=['time_create','question']



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
class Universities(models.Model):
    slug= models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    name = models.CharField(max_length=100, db_index=True,verbose_name="Название института")
    def __str__(self):
        return self.name
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фотография", blank=True)
    class Meta:
        verbose_name = 'Университет'
        verbose_name_plural = 'Университеты'
    def get_absolute_url(self):
        return reverse('universities', kwargs={'university_slug':self.slug})
class Comments(models.Model):
    cat = models.ForeignKey('Category',on_delete=models.PROTECT, null=True, verbose_name="Категория")


