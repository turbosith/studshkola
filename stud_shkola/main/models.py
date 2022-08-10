from django.db import models

class questions(models.Model):
    question=models.TextField('Вопрос')
    category=models.CharField('Тематика', max_length=100)
    def __str__(self):
        return self.question
    class Meta:
        verbose_name='Вопрос'
        verbose_name_plural = 'Вопросы'

