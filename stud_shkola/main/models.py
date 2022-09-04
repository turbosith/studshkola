from django.db import models
from django.urls import reverse

categ={}
class questions(models.Model):
    cat = models.ForeignKey('Category',on_delete=models.PROTECT, null=True)
    question=models.TextField( blank=True, verbose_name="Вопрос")
    photo=models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фотография",blank=True)
    userid = models.BigIntegerField(default=0)
    time_create=models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering=['time_create','question']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,verbose_name="Категория")
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id':self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']



