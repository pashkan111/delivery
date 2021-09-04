from .models import Calculate, Term
from rest_framework.response import Response


def check_volume(volume, weight):
    new_volume = volume*240
    if new_volume > weight:
        return new_volume
    return weight


def get_price(
        cityto_id,
        cityfrom_id,
        weight,
        volume,
        delivery_from,
        delivery_to
    ):
    weight = check_volume(volume=volume, weight=weight)
    object = Calculate.objects.filter(
        cityto=cityto_id,
        cityfrom=cityfrom_id,
        weightfrom__lte=weight,
        weightto__gte=weight,
        )
    if not object:
        return 0, 0, 0, 0, 0, 0
    object = object.first()
    price_standart = object.inter_terminal
    price_to_address = object.delivery_to
    price_from_address = object.delivery_from
    price_express = price_standart * 1.3
    convert_price = object.convert_price
    if delivery_from:
        delivery_from = object.delivery_from
    if delivery_to:
        delivery_to = object.delivery_to
    price_standart = delivery_from + price_standart + delivery_to
    price_express = delivery_from + price_express + delivery_to
    return price_standart, price_express, convert_price, object.inter_terminal, delivery_to, delivery_from
    # return price_standart, price_express, convert_price, object.inter_terminal, price_to_address, price_from_address
    

def get_time_to_deliver(cityto_id, cityfrom_id):
    data = Term.objects.filter(
        cityto_id=cityto_id,
        cityfrom_id=cityfrom_id
    )
    if not data:
        return False
    data = data.first()
    term_standart_from = data.term_standart_from
    term_standart_to = data.term_standart_to
    term_express_from = data.term_express_from
    term_express_to = data.term_express_to
    result = {
        'term_standart_from': term_standart_from,
        'term_standart_to': term_standart_to,
        'term_express_from': term_express_from,
        'term_express_to': term_express_to
    }
    return result
    
   
    
