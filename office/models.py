from django.db import models
from calculator.models import City


class Office(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='office_of_city', db_index=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    coordinates = models.CharField(max_length=255, verbose_name='Координаты', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы' 