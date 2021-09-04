from django.db import models
from django.core.validators import MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class OrderConsignment(models.Model):

    TYPE_TRANS = (
        ('Стандарт', 'Стандарт'),
        ('Экспресс', 'Экспресс'),
        ('Конверт', 'Конверт'),
    )
    
    PAY = (
        ('Наличный расчет', 'Наличный расчет'),
        ('Безналичный расчет', 'Безналичный расчет'),
        ('Карта', 'Карта'),
    )
    
    INTERVAL = (
        ('6:00', '6:00'),
        ('7:00', '7:00'),
        ('8:00', '8:00'),
        ('9:00', '9:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
        ('20:00', '20:00'),
        ('21:00', '21:00'),
        ('22:00', '22:00'),
        ('23:00', '23:00'),
    )
    
    DOCUMENTS = (
        ('Паспорт', 'Паспорт'),
        ('Заграничный паспорт', 'Заграничный паспорт'),
        ('Военный билет', 'Военный билет'),
        ('Водительское удостоверение', 'Водительское удостоверение'),
    )
    PERSON = (
        ('Отправитель', 'Отправитель'),
        ('Получатель', 'Получатель'),
        ('Третье лицо', 'Третье лицо'),
    )
    SUM = (
        ('По чеку на адресе', 'По чеку на адресе'),
        ('Включить в счет', 'Включить в счет'),
    )
    
    
    city_to = models.CharField(verbose_name='Куда', max_length=255, blank=True, null=True)
    city_from = models.CharField(verbose_name='Откуда', max_length=255, blank=True, null=True)
    address_from = models.CharField(verbose_name='Адрес', max_length=255, blank=True, null=True)
    terminal_from = models.CharField(verbose_name='Терминал', max_length=255, blank=True, null=True)
    address_to = models.CharField(verbose_name='Адрес', max_length=255, blank=True, null=True)
    terminal_to = models.CharField(verbose_name='Терминал', max_length=255, blank=True, null=True)
    date_cargo = models.DateField('Дата забора груза', blank=True, null=True)
    type_transporation = models.CharField(verbose_name='Вид перевозки',choices=TYPE_TRANS, max_length=50, default='Стандарт')
    nature_cargo = models.CharField(verbose_name='Характер груза', max_length=255, blank=True, null=True)
    #интервал
    interval1 = models.CharField(verbose_name='Время доставки, от', choices=INTERVAL, max_length=50, default='9:00')
    interval2 = models.CharField(verbose_name='Время доставки, до', choices=INTERVAL, max_length=50, default='18:00')
    #1место
    length_one = models.DecimalField(verbose_name='Длина(м)', max_digits=8, decimal_places=3, blank=True, null=True, default=0.1)
    width_one = models.DecimalField(verbose_name='Ширина(м)', max_digits=8, decimal_places=3, blank=True, null=True, default=0.1)
    height_one = models.DecimalField(verbose_name='Высота(м)', max_digits=8, decimal_places=3, blank=True, null=True, default=0.1)
    weight_one = models.DecimalField(verbose_name='Вес(кг)' , max_digits=8, decimal_places=3, blank=True, null=True, default=1)
    volume_one = models.DecimalField(verbose_name='Объем(м3)', max_digits=8, decimal_places=3, blank=True, null=True, default=0.001)

    #несколько мест
    some_weight = models.DecimalField(verbose_name='Общий вес(кг)', max_digits=8, decimal_places=3, blank=True, null=True, default=0.1)
    some_volume = models.DecimalField(verbose_name='Общий объем(м3)', max_digits=8, decimal_places=3, blank=True, null=True, default=0.001)
    some_place_quantity = models.DecimalField(verbose_name='Кол-во мест', max_digits=8, decimal_places=3, blank=True, null=True, default=2)
    some_longest = models.DecimalField(verbose_name='Самое длинное(м)', max_digits=8, decimal_places=3, blank=True, null=True, default=0.1)
    some_widest = models.DecimalField(verbose_name='Самое широкое(м)', max_digits=8, decimal_places=3, blank=True, null=True, default=0.1)
    some_highest = models.DecimalField(verbose_name='Самое высокое(м)', max_digits=8, decimal_places=3, blank=True, null=True, default=0.1)
    #документы
    
    document_length = models.DecimalField(verbose_name='Длина(см)', max_digits=5, decimal_places=2,  blank=True, null=True, default=31)
    document_width = models.DecimalField(verbose_name='Ширина(см)', max_digits=5, decimal_places=2,  blank=True, null=True, default=25)
    document_height = models.DecimalField(verbose_name='Высота(см)', max_digits=5, decimal_places=2,  blank=True, null=True, default=3)
    document_weight =  models.DecimalField(verbose_name='Вес(кг)', max_digits=5, decimal_places=2,  blank=True, null=True, default=2)
    #доп услуги
    
    category = models.CharField(default='1place', max_length=20, blank=True, null=True)
    
    declared_value = models.PositiveIntegerField(verbose_name='Объявленная стоимость', blank=True, null=True, default=1)
    insurance = models.BooleanField(verbose_name='Страховка')
    return_of_accompanying_documents = models.BooleanField(verbose_name='Возврат сопроводительных документов')
    sending_accompanying_documents = models.BooleanField(verbose_name='Отправка сопроводительных документов')
    loading_and_unloading_sender = models.BooleanField(verbose_name='Погрузо-разгрузочные работы у отправителя')
    service_lift_sender = models.BooleanField(verbose_name='Наличие грузового лифта', default='')
    floor_sender = models.PositiveIntegerField(verbose_name='Поднятие(этаж)', blank=True, null=True, default=0)
    carry_sender = models.PositiveIntegerField(verbose_name='Пронос(м)', blank=True, null=True, default=0)
    loading_and_unloading_recipient = models.BooleanField(verbose_name='Погрузо-разгрузочные работы у получателя')
    service_lift_recipient = models.BooleanField(verbose_name='Наличие грузового лифта', default='')
    floor_recipient = models.PositiveIntegerField(verbose_name='Поднятие(этаж)', blank=True, null=True, default=0)
    carry_recipient = models.PositiveIntegerField(verbose_name='Пронос(м)', blank=True, null=True, default=0)
    pass_sender_territory = models.BooleanField(verbose_name='Пропуск на территорию отправителя')
    order_per_hour = models.BooleanField(verbose_name='Заказать за час', default='')
    order_per_day = models.BooleanField(verbose_name='Заказать за сутки', default='')
    registration_for_shipment = models.BooleanField(verbose_name='Запись на отгрузку')
    paid_entry_sender_territory = models.BooleanField(verbose_name='Платный въезд на территорию отправителя')
    sum = models.DecimalField(verbose_name='Сумма', max_digits=10, decimal_places=2, blank=True, null=True)
    reimbursement_method = models.CharField(verbose_name='Способ возмещения суммы', choices=SUM, max_length=50, default='Включить в счет', blank=True, null=True)
    internal_shipment_number = models.BooleanField(verbose_name='Внутренний номер отгрузки')
    info_internal_shipment_number = models.CharField(verbose_name='', max_length=255, blank=True, null=True)
    cod = models.BooleanField(verbose_name='Наложенный платеж')
    cod_input = models.DecimalField(verbose_name='Сумма наложенного платежа', max_digits=10, decimal_places=2, blank=True, null=True)
    second_address = models.BooleanField(verbose_name='Заезд на второй адрес')
    check_second_address= models.CharField(verbose_name='Город и адрес', max_length=255, blank=True, null=True)
    delivery_confirmation = models.BooleanField(verbose_name='Подтверждение доставки')
    power_of_attorney = models.BooleanField(verbose_name='Доверенность')
    info_proxy = models.CharField(verbose_name='', max_length=255, blank=True, null=True)
    pre_call = models.BooleanField(verbose_name='Предварительный звонок')
    callback_one_hour = models.BooleanField(verbose_name='Отзвон за 1 час', default='')
    callback_two_hour = models.BooleanField(verbose_name='Отзвон за 2 час', default='')
    #упаковка груза
    
    rigid_packaging = models.BooleanField(verbose_name='Жесткая упаковка')
    rigid_packaging_amount = models.DecimalField(default=1,max_digits=5, decimal_places=2, verbose_name='Укажите количество')
    pallet_board = models.BooleanField(verbose_name='Паллетный борт')
    pallet_board_amount = models.DecimalField(default=1, max_digits=5, decimal_places=2,verbose_name='Укажите количество')
    bag = models.BooleanField(verbose_name='Мешок')
    bag_amount = models.PositiveIntegerField(default=1, verbose_name='Укажите количество')
    cardboard_box = models.BooleanField(verbose_name='Картонная коробка')
    cardboard_box_amount = models.PositiveIntegerField(default=1, verbose_name='Укажите количество')
    pallet = models.BooleanField(verbose_name='Палет')
    pallet_amount = models.PositiveIntegerField(default=1, verbose_name='Укажите количество')
    strapping = models.BooleanField(verbose_name='Стреппинг')
    strapping_amount = models.DecimalField(default=1,max_digits=5, decimal_places=2, verbose_name='Укажите количество')
    stretch = models.BooleanField(verbose_name='Стрейч - пленка')
    stretch_amount = models.DecimalField(default=1,max_digits=5, decimal_places=2, verbose_name='Укажите количество')
    air_bubble = models.BooleanField(verbose_name='Воздушно - пузырьковая пленка')
    air_bubble_amount = models.DecimalField(default=1,max_digits=5, decimal_places=2, verbose_name='Укажите количество')
    #участники грузоперевозок
    
    #Заказчик
    #физлицо
    fio_individual = models.CharField(verbose_name='ФИО', max_length=255, blank=True, null=True)
    documents = models.CharField(verbose_name='Выберите тип документа', choices=DOCUMENTS, max_length=50, default='Паспорт', blank=True, null=True)
    passport_individual = models.CharField(verbose_name='Серия и номер выбранного документа', max_length=11, blank=True, null=True)
    email_individual = models.CharField(verbose_name='Email', max_length=255, blank=True, null=True)
    phone_individual = models.CharField(verbose_name='Контактный телефон', blank=True, unique=True, null=True, max_length=255)
    #юрлицо
    fio_entity = models.CharField(verbose_name='Название компании', max_length=255, blank=True, null=True)
    inn_entity = models.IntegerField(verbose_name='ИНН', blank=True, null=True)
    contact_person_entity = models.CharField(verbose_name='Контактное лицо', max_length=255, blank=True, null=True)
    email_entity = models.CharField(verbose_name='Email', max_length=255, blank=True,  null=True)
    phone_entity = models.CharField(verbose_name='Контактный телефон', blank=True, unique=True,  null=True, max_length=255)


    #Получатель
    #физлицо
    fio_individual_p = models.CharField(verbose_name='ФИО', max_length=255, blank=True, null=True)
    documents_p = models.CharField(verbose_name='Выберите тип документа', choices=DOCUMENTS, max_length=50, default='Паспорт', blank=True, null=True)
    passport_individual_p = models.CharField(verbose_name='Серия и номер выбранного документа', max_length=11, blank=True, null=True)
    email_individual_p = models.CharField(verbose_name='Email', max_length=255, blank=True, null=True)
    phone_individual_p = models.CharField(verbose_name='Контактный телефон', blank=True, unique=True, null=True, max_length=255)
    #юрлицо
    fio_entity_p = models.CharField(verbose_name='Название компании', max_length=255, blank=True, null=True)
    inn_entity_p = models.IntegerField(verbose_name='ИНН', blank=True, null=True)
    contact_person_entity_p = models.CharField(verbose_name='Контактное лицо', max_length=255, blank=True, null=True)
    email_entity_p = models.CharField(verbose_name='Email', max_length=255, blank=True,  null=True)
    phone_entity_p = models.CharField(verbose_name='Контактный телефон', blank=True, unique=True,  null=True, max_length=255)

    
    #плательщик
    sender_payer = models.BooleanField(verbose_name='Отправитель')
    recipient_payer = models.BooleanField(verbose_name='Получатель')
    #заказчик
    sender_customer = models.BooleanField(verbose_name='Отправитель')
    recipient_customer = models.BooleanField(verbose_name='Получатель')
    #третье лицо
    third_person_input_payer = models.CharField(verbose_name='Город, имя, телефон', max_length=300, blank=True, null=True)
    third_person_input_customer = models.CharField(verbose_name='Город, имя, телефон', max_length=300, blank=True, null=True)
    pay_cargo = models.CharField(verbose_name='Форма оплаты', choices=PAY, max_length=50, default=PAY[0])
    comment = models.CharField(verbose_name='Комментарий', max_length=10000, blank=True, null=True)

class OrderStatusConsignment(models.Model):
    STATUS_CHOICES = (
        ('Принято', 'ПРИНЯТО'),
        ('Ожидается забор груза', 'ОЖИДАЕТСЯ ЗАБОР ГРУЗА'),
        ('Ожидается доставка груза', 'ОЖИДАЕТСЯ ДОСТАВКА ГРУЗА'),
        ('Принято на склад отправки', 'ПРИНЯТО НА СКЛАД ОТПРАВКИ'),
        ('Ожидается отправка', 'ОЖИДАЕТСЯ ОТПРАВКА'),
        ('В пути', 'В ПУТИ'),
        ('В пути до терминала', 'В ПУТИ'),
        ('Доставка другой транспортной компанией','В ПУТИ'),
        ('Прибыло на склад получения', 'ПРИБЫЛО НА СКЛАД ПОЛУЧЕНИЯ'),
        ('Готово к выдаче', 'ГОТОВО К ВЫДАЧЕ'),
        ('Выдано', 'ВЫДАНО'),
        ('Прибыло на склад транзита', 'ПРИБЫЛО НА СКЛАД ТРАНЗИТА'),
    )
    
    order_number = models.CharField(max_length=255, blank=False, unique=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='Уточняется')
    delivery_date = models.DateField(blank=False)
    

# class Packing(models.Model):
#     name = models.CharField(max_length=255, verbose_name=)
    


class Cities(models.Model):
    cities = models.CharField(max_length=255)

    def __str__(self):
        return self.cities