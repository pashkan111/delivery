from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    @classmethod
    def get_count(cls):
        return cls.objects.all().count()

    def __str__(self) -> str:
        return self.name


class Calculate(models.Model):
    cityfrom = models.ForeignKey(City, on_delete=models.CASCADE, related_name='calc_cityfrom')
    cityto = models.ForeignKey(City, on_delete=models.CASCADE, related_name='calc_cityto')
    weightfrom = models.DecimalField(max_digits=9, decimal_places=2)
    weightto = models.DecimalField(max_digits=9, decimal_places=2)
    inter_terminal = models.IntegerField()
    delivery_from = models.IntegerField()
    delivery_to = models.IntegerField()
    convert_price = models.IntegerField()

    def __str__(self):
        return f'''Город отправления: {self.cityfrom};
                    город доставки: {self.cityto};
                    вес от: {self.weightfrom};
                    вес до: {self.weightto};
                    межтерминальная: {self.inter_terminal};
                    доставка от: {self.delivery_from};
                    доставка до: {self.delivery_to}
                '''


class Term(models.Model):
    cityfrom = models.ForeignKey(City, on_delete=models.CASCADE, related_name='term_cityfrom')
    cityto = models.ForeignKey(City, on_delete=models.CASCADE, related_name='term_cityto')
    term_standart_from = models.IntegerField()
    term_standart_to = models.IntegerField()
    term_express_from = models.IntegerField()
    term_express_to = models.IntegerField()

    def __str__(self):
        return f'{self.cityto}'


