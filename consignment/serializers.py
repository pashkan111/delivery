from django.db.models import fields
from rest_framework import serializers 
from .models import TrackStatusConsignment, OrderConsignment, OrderStatusConsignment, Cities

class TrackStatusConsignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrackStatusConsignment
        fields = ('id',
                  'tracking_number',
                  'status',
                  'delivery_date',
                  'status_pay',
                  'route')


class OrderConsignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderConsignment
        fields = ('id',
                  'city_from',
    'city_to',
    'from_address',
    'to_address' ,
    'customer_name' ,
    'recipient',
    'payer' ,
    'sender',
    'fence_address',
    'delivery_address',
    'fence_date',
    'fence_interval',
    'quantity_places',
    'quantity_weight',
    'quantity_volume',
    'delivery_type'
                  )


class OrderStatusConsignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderStatusConsignment
        fields = ('id',
                  'order_number',
                 'status',
                 'delivery_date')


class CitiesSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Cities
        fields = ('id',
                'cities')