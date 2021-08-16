from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view

from calculator.models import Calculate, Term, City
from calculator.serializers import CalculateSerializer, TermSerializer, CitySerializer

import json
# Create your views here.

def calc(request):

    context = { 
        'is_worker': request.user.groups.filter(name='worker').exists(),
    }
    
    return render(request, 'calculator.html', context)


def calc_post(request):
    struct = request.POST.get('struct')
    weight = float(struct[3])
    volume = float(struct[4])
    # todo
    volume_weight = volume * 240
    max_weight = max(weight, volume_weight)
    
    response = Calculate.objects.filter(cityto__exact=struct[0]).filter(cityfrom__exact=struct[1]).filter(weightto__gte=str(max_weight))
    #response_term = Term.objects.filter(cityto__exact=struct[0]).filter(cityfrom__exact=struct[1]).filter
    res_calc = {
        'cityto': response[0][0],
        'cityfrom': response[0][1],    
        'weightto': response[0][2],  
        'weightfrom': response[0][3],
        'inter_terminal': response[0][4],
        'pickup': response[0][5],
        'cargo_delivery': response[0][6],
    }

    return json.dumps(res_calc)


@api_view(['GET', 'POST'])
def create_calculate(request):  
    if request.method == 'GET':
        calc_api = Calculate.objects.all()
        calc_api_serializer = CalculateSerializer(calc_api, many=True)
        return JsonResponse(calc_api_serializer.data, safe=False)

    elif request.method == 'POST':
        calc_api_data = JSONParser().parse(request)
        calc_api_serializer = CalculateSerializer(data=calc_api_data, many=True)
        if calc_api_serializer.is_valid():
            calc_api_serializer.save()
            return JsonResponse(calc_api_serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(calc_api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_calculate(request, pk):
    try:
        calc_api = Calculate.objects.get(pk=pk)
    except Calculate.DoesNotExist:
        return JsonResponse({'message': 'Накладной не существует'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        calc_api_data = JSONParser().parse(request)
        calc_api_serializer = CalculateSerializer(calc_api, data=calc_api_data)
        if calc_api_serializer.is_valid():
            calc_api_serializer.save()
            return JsonResponse(calc_api_serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(calc_api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def create_term(request):  
    if request.method == 'GET':
        term_api = Term.objects.all()
        term_api_serializer = TermSerializer(term_api, many=True)
        return JsonResponse(term_api_serializer.data, safe=False)

    elif request.method == 'POST':
        term_api_data = JSONParser().parse(request)
        term_api_serializer = TermSerializer(data=term_api_data, many=True)
        if term_api_serializer.is_valid():
            term_api_serializer.save()
            return JsonResponse(term_api_serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(term_api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_term(request, pk):
    try:
        term_api = Term.objects.get(pk=pk)
    except Term.DoesNotExist:
        return JsonResponse({'message': 'Накладной не существует'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        term_api_data = JSONParser().parse(request)
        term_api_serializer = TermSerializer(term_api, data=term_api_data)
        if term_api_serializer.is_valid():
            term_api_serializer.save()
            return JsonResponse(term_api_serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(term_api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_availible_countries(request):
    data = City.objects.all()
    cities = CitySerializer(data, many=True)
    print(cities.data)
    # return JsonResponse({'c':'3434'})
    return Response(cities.data)
