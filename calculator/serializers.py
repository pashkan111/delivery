from rest_framework import serializers 

from calculator.models import Calculate, Term, City


class CalculateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calculate
        fields = ('id',
                  'cityto',
                  'cityfrom',
                  'weightto',
                  'weightfrom',
                  'inter_terminal',
                  'pickup',
                  'cargo_delivery',
                  'premium')


class TermSerializer(serializers.ModelSerializer):

    class Meta:
        model = Term
        fields = ('cityto',
                  'cityfrom',
                  'term_standart_to',
                  'term_standart_from',
                  'term_express_to',
                  'term_express_from')

class CitySerializer(serializers.ModelSerializer):
    # count = serializers.SerializerMethodField()

    class Meta:
        model=City
        fields=('name',)

    # def get_count(self, obj):
    #     return obj.get_count()
    