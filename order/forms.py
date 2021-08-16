from django import forms
from django.forms.widgets import Textarea, CheckboxInput

from consignment.models import OrderConsignment


class DateInput(forms.DateInput):
    input_type = 'date'


class OrderForm(forms.ModelForm):
    nature_cargo = forms.CharField(label='Характер груза',
                                   help_text='Грузы подлежащие обязательной упаковке могут быть приняты к перевозке '
                                             'без услуги "Упаковка" в случае наличия у отправителя надлежащей '
                                             'заводской '
                                             'упаковки, в противном случае груз не будет принят к перевозке')
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
