from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    STATUS = (
        (0, 'Не опубликован'),
        (1, 'Опубликован')
    )
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('URL', max_length=200, unique=True)
    text = models.TextField('Основной текст', max_length=10000)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField('Дата публикации', default=timezone.now)
    status = models.IntegerField('Статус', choices=STATUS, default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']   
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости' 
        