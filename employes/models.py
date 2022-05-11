from django.db import models

class Employes(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Имя')
    age = models.IntegerField(
        blank=True,
        verbose_name='Возраст')
    salary = models.IntegerField(
        default=20000,
        blank=True,
        verbose_name='Зарплата')
    skill = models.IntegerField(
        blank=True,
        verbose_name='Опыт работы')
    image = models.ImageField(
        upload_to='image/%Y/%m/%d',
        blank=True,
        verbose_name='Фотки')
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания')    
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления')    
    public = models.BooleanField(
        default=True,
        verbose_name='Опубликованно')