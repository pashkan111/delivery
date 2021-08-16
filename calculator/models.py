from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    @classmethod
    def get_count(cls):
        return cls.objects.all().count()

    def __str__(self) -> str:
        return self.name


class Calculate(models.Model):
    cityto = models.ForeignKey(City, on_delete=models.CASCADE, related_name='calc_cityto')
    cityfrom = models.ForeignKey(City, on_delete=models.CASCADE, related_name='calc_cityfrom')
    # weightto = models.DecimalField(max_digits=9, decimal_places=2)
    # weightfrom = models.DecimalField(max_digits=9, decimal_places=2)
    # inter_terminal = models.IntegerField()
    weightto = models.CharField(max_length=255)
    weightfrom = models.CharField(max_length=255)
    inter_terminal = models.CharField(max_length=255)
    pickup = models.CharField(max_length=255)

    def __str__(self):
        return f'from {self.cityfrom} to {self.cityto}'


class Term(models.Model):
    cityto = models.ForeignKey(City, on_delete=models.CASCADE, related_name='term_cityto')
    cityfrom = models.ForeignKey(City, on_delete=models.CASCADE, related_name='term_cityfrom')
    term_standart_to = models.CharField(max_length=255)
    term_standart_from = models.CharField(max_length=255)
    term_express_to = models.CharField(max_length=255)
    term_express_from = models.CharField(max_length=255)
    # term_standart_to = models.IntegerField()
    # term_standart_from = models.IntegerField()
    # term_express_to = models.IntegerField()
    # term_express_from = models.IntegerField()

    def __str__(self):
        return self.cityto


