from copy import Error
from django import forms
from django.forms.widgets import Textarea, CheckboxInput
from calculator.models import City
from consignment.models import OrderConsignment


class DateInput(forms.DateInput):
    input_type = 'date'


class OrderForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['document_length'].widget.attrs['readonly'] = True
        self.fields['document_width'].widget.attrs['readonly'] = True
        self.fields['document_height'].widget.attrs['readonly'] = True
        self.fields['document_weight'].widget.attrs['readonly'] = True
        
        self.fields['rigid_packaging_amount'].widget.attrs['min'] = 1
        self.fields['pallet_board_amount'].widget.attrs['min'] = 1
        self.fields['bag_amount'].widget.attrs['min'] = 1
        self.fields['cardboard_box_amount'].widget.attrs['min'] = 1
        self.fields['pallet_amount'].widget.attrs['min'] = 1
        self.fields['strapping_amount'].widget.attrs['min'] = 1
        self.fields['stretch_amount'].widget.attrs['min'] = 1
        self.fields['air_bubble_amount'].widget.attrs['min'] = 1

        self.fields['rigid_packaging_amount'].widget.attrs['max'] = 100000
        self.fields['pallet_board_amount'].widget.attrs['max'] = 100000
        self.fields['bag_amount'].widget.attrs['max'] = 100000
        self.fields['cardboard_box_amount'].widget.attrs['max'] = 100000
        self.fields['pallet_amount'].widget.attrs['max'] = 100000
        self.fields['strapping_amount'].widget.attrs['max'] = 100000
        self.fields['stretch_amount'].widget.attrs['max'] = 100000
        self.fields['air_bubble_amount'].widget.attrs['max'] = 100000
        
        
        self.fields['floor_sender'].widget.attrs['max'] = 500
        
    nature_cargo = forms.CharField(label='Характер груза',
                                   help_text='Грузы подлежащие обязательной упаковке могут быть приняты к перевозке '
                                             'без услуги "Упаковка" в случае наличия у отправителя надлежащей '
                                             'заводской '
                                             'упаковки, в противном случае груз не будет принят к перевозке', required=False)
    return_of_accompanying_documents = forms.BooleanField(label='Возврат сопроводительных документов',
                                                          help_text='Стоимость услуги 250 рублей', required=False)
    sending_accompanying_documents = forms.BooleanField(label='Отправка сопроводительных документов',
                                                        help_text='Стоимость услуги 50 рублей', required=False)
    delivery_confirmation = forms.BooleanField(label='Подтверждение доставки',
                                               help_text='Стоимость услуги 125 рублей', required=False)
    rigid_packaging = forms.BooleanField(label='Жесткая упаковка',
                                         help_text='Стоимость упаковки: 600 рублей за м3, минимальная стоимость '
                                                   '— 600 руб.', required=False)
    pallet_board = forms.BooleanField(label='Паллетный борт',
                                      help_text='Стоимость упаковки: 600 рублей за м3, минимальная стоимость '
                                                '— 600 руб.', required=False)
    bag = forms.BooleanField(label='Мешок',
                             help_text='Грузоподъемность одного мешка не более 25 кг. Стоимость упаковки: 80 '
                                       'рублей за единицу.', required=False)
    cardboard_box = forms.BooleanField(label='Картонная коробка',
                                       help_text='Размеры и стоимости коробок:'
                                                 '1. 0,2 х 0,19 х  0,13 м, вес груза до 2 кг- 40 рублей за штуку'
                                                 '2. 0,3 х 0,25 х 0,17 м, вес груза до 5 кг- 70 рублей за штуку'
                                                 '3. 0,3 х 0,26 х 0,38 м, вес до 12 кг- 100 рублей за штуку'
                                                 '', required=False)
    pallet = forms.BooleanField(label='Палет',
                                help_text='Стоимость: 160 рублей за паллет.', required=False)
    strapping = forms.BooleanField(label='Стреппинг',
                                   help_text='Стоимость: 100 рублей за м3, минимальная стоимость — 100 руб.',
                                   required=False)
    stretch = forms.BooleanField(label='Стрейч - пленка',
                                 help_text='Стоимость упаковки: 150 рублей за м3, минимальная стоимость — 150 руб.',
                                 required=False)
    air_bubble = forms.BooleanField(label='Воздушно - пузырьковая пленка',
                                    help_text='Стоимость упаковки: 150 рублей за м3, минимальная стоимость — 150 руб.',
                                    required=False)

    class Meta:
        model = OrderConsignment
        fields = '__all__'
        widgets = {
            'date_cargo': DateInput(), 'comment': Textarea(), 'sender_payer': CheckboxInput(attrs={'class': 'as'}),
            'recipient_payer': CheckboxInput(attrs={'class': 'as'}),
            'sender_customer': CheckboxInput(attrs={'class': 'as1'}),
            'recipient_customer': CheckboxInput(attrs={'class': 'as1'}),
        }
        
    # def clean_length_one(self, **kwargs):
    #     length_one = self.cleaned_data['length_one']
    #     if float(length_one) > 3:
    #         msg = "Максимальное значение - 3м"
    #         self.add_error('length_one', msg)
    #     return length_one        

    # def clean_weight_one(self, **kwargs):
    #     weight_one = self.cleaned_data['weight_one']
    #     if float(weight_one) > 500:
    #         msg = "Максимальное значение - 500кг"
    #         self.add_error('weight_one', msg)
    #     return weight_one 

    # def clean_width_one(self, **kwargs):
    #     width_one = self.cleaned_data['width_one']
    #     if float(width_one) > 3:
    #         msg = "Максимальное значение - 3м"
    #         self.add_error('width_one', msg)
    #     return width_one

    # def clean_height_one(self, **kwargs):
    #     height_one = self.cleaned_data['height_one']
    #     if float(height_one) > 3:
    #         msg = "Максимальное значение - 3м"
    #         self.add_error('height_one', msg)
    #     return height_one

    # def clean_city_to(self, **kwargs):
    #     city_to = self.cleaned_data['city_to']
    #     cities = City.objects.all().values('name')
    #     if city_to not in cities:
    #         msg = "Выберите город из выпадающего списка"
    #         self.add_error('city_to', msg)
    #     return city_to 

    # def clean_city_from(self, **kwargs):
    #     city_from = self.cleaned_data['city_from']
    #     cities = City.objects.all().values('name')
    #     if city_from not in cities:
    #         msg = "Выберите город из выпадающего списка"
    #         self.add_error('city_from', msg)
    #     return city_from 