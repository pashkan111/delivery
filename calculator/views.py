from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from calculator.models import Calculate, Term, City
from calculator.serializers import CalculateSerializer, TermSerializer, CitySerializer
import json
from .services import get_price, get_time_to_deliver
from loguru import logger


logger.add('logs/debug_calculator.log', format="{time} {level}, {message}", level="DEBUG", rotation='100 KB')

def calc(request): 
    return render(request, 'calculator.html')


class PostCalculate(APIView):

    def post(self, request):
        calc_data = dict(request.data)
        try:
            cityto_name = calc_data.get('cityto')
            cityfrom_name = calc_data.get('cityfrom')
            weight = float(calc_data.get('weight'))
            volume = float(calc_data.get('volume'))
            delivery_from = calc_data.get('delivery_from', 0)
            delivery_to = calc_data.get('delivery_to', 0)
        except KeyError as ke:
            logger.error(f'{ke}')
            message = {'status': 'no data'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        cityto_id = City.objects.filter(name=cityto_name).first().id
        cityfrom_id = City.objects.filter(name=cityfrom_name).first().id
        if cityto_id and cityfrom_id:
            try:
                price_standart, price_express, convert_price, inter_terminal, price_to_address, price_from_address = get_price(
                    cityto_id,
                    cityfrom_id,
                    weight,
                    volume,
                    delivery_from,
                    delivery_to
                )
                if not (price_standart,  price_express, convert_price):
                    return Response('data with such parametrs does not exist')
            except Exception as ex:
                logger.error(ex)
                return Response(f'error: {ex}', status=status.HTTP_400_BAD_REQUEST)
            times = get_time_to_deliver(cityto_id, cityfrom_id)
            data = {
                'price_standart': price_standart,
                'price_express': price_express,
                'convert_price': convert_price,
                'inter_terminal': inter_terminal,
                'price_to_address': price_to_address, 
                'price_from_address': price_from_address,
                'times': times
            }
            logger.info(f'{data} has been sent to frontend')
            return Response(json.dumps(data))
        else:
            logger.error('Such city does not exist')
            return Response('Such city does not exist')


class PutCalculatorData(APIView):

    def post(self, request):
        data = request.data
        try:
            cityto_name = data['cityto']
            cityfrom_name = data['cityfrom']
            weightfrom = data['weightfrom']
            weightto = data['weightto']
            inter_terminal = data['inter_terminal']
            delivery_from = data['delivery_from']
            delivery_to = data['delivery_to']
            convert_price = data['convert_price']
        except KeyError as ke:
            logger.error(f'{ke}')
            return Response(f'{ke}')   
        if cityfrom_name and cityfrom_name:
            new_cityto, created = City.objects.get_or_create(name=cityto_name)
            new_cityfrom, created = City.objects.get_or_create(name=cityfrom_name)
            cityto_id = new_cityto.id
            cityfrom_id = new_cityfrom.id      
            new_calculator, created = Calculate.objects.get_or_create(                cityto=new_cityto,
                cityfrom=new_cityfrom,
                weightfrom=weightfrom,
                weightto=weightto,
                inter_terminal=inter_terminal,
                delivery_from=delivery_from,
                delivery_to=delivery_to,
                convert_price=convert_price    
            )
            if new_calculator:
                logger.info(f'{new_calculator.__str__()} has been created')
        return Response('ok')


class PutTermData(APIView):
    
    def post(self, request):
        data = request.data
        for lst in data:
            try:
                cityto_name = lst['cityto']
                cityfrom_name = lst['cityfrom']
                term_standart_from = lst['term_standart_from']
                term_standart_to = lst['term_standart_to']
                term_express_from = lst['term_express_from']
                term_express_to = lst['term_express_to']
            except KeyError as ke:
                logger.error(f'{ke}')     
                return Response(f'{ke}')
            if cityfrom_name and cityfrom_name:
                new_cityto, created = City.objects.get_or_create(name=cityto_name)
                new_cityfrom, created = City.objects.get_or_create(name=cityfrom_name)
                cityto_id = new_cityto.id
                cityfrom_id = new_cityfrom.id
                new_term, created = Term.objects.get_or_create(
                    cityto=new_cityto,
                    cityfrom=new_cityfrom,
                    term_standart_from=term_standart_from,
                    term_standart_to=term_standart_to,
                    term_express_from=term_express_from,
                    term_express_to=term_express_to,
                )
                if new_term:
                    logger.info(f'{new_term.__str__()} has been created')
        return Response('ok')
        # return Response('ok')
        
            
@api_view(['GET'])
def get_availible_cities(request):
    data = City.objects.all().only('name')
    cities = CitySerializer(data, many=True)
    return Response(cities.data)