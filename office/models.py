from django.db import models


# Create your models here.

class Office(models.Model):
    city = models.CharField('Город', max_length=10000)
    text = models.TextField('Основной текст', max_length=10000)


    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы' 