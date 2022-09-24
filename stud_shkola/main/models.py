from django.db import models
from django.urls import reverse

categ={}
class Questions(models.Model):
    cat = models.ForeignKey('Category',on_delete=models.PROTECT, null=True, verbose_name="Категория")
    question=models.TextField( blank=True, verbose_name="Вопрос")
    photo=models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фотография",blank=True)
    userid = models.BigIntegerField(default=0)
    uni = models.ForeignKey('Universities', on_delete=models.PROTECT, null=True, verbose_name="Вузы")
    time_create=models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True, verbose_name="Опубликовано")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.question
    def get_absolute_url(self):
        return reverse('que', kwargs={'que_slug':self.slug})
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
        return reverse('category', kwargs={'cat_slug': self.slug})

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
        return reverse('university', kwargs={'university_slug':self.slug})



