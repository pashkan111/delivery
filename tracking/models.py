from django.db import models

class Tracking(models.Model):
    
    STATUS_CHOICES = (
    ('In_awaiting_of_delivering_cargo', 'ОЖИДАЕТСЯ ДОСТАВКА ГРУЗА'),
    ('Accepted_on_sklad_otpravki', 'ПРИНЯТО НА СКЛАД ОТПРАВКИ'),
    ('In_expecting_0f_otpravka', 'ОЖИДАЕТСЯ ОТПРАВКА'),
    ('V_puti', 'В ПУТИ'),
    ('Pribilo_na_sklad_poluchenia', 'ПРИБЫЛО НА СКЛАД ПОЛУЧЕНИЯ'),
    ('Gotovo_k_vidache', 'ГОТОВО К ВЫДАЧЕ'),
    ('Vidano', 'ВЫДАНО'),
    ('Pribilo_na_sklad_tranzita', 'ПРИБЫЛО НА СКЛАД ТРАНЗИТА'),
)

    STATUSPAY_CHOICES = (
        ('paid', 'ОПЛАЧЕНО'),
        ('not_paid', 'НЕ ОПЛАЧЕНО'),
    )

    tracking_number_client = models.CharField(max_length=200)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='Уточняется')
    status_date = models.DateField(auto_now_add=True)
    status_pay = models.CharField(choices=STATUSPAY_CHOICES, max_length=50, default='Уточняется')
    route = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return f'trek: {self.trek}, status: {self.status}'