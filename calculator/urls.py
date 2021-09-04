from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from calculator.views import calc
from calculator import views


urlpatterns = [
    path('calc/', calc, name='calc'),
    path('api/post-calc', csrf_exempt(views.PostCalculate.as_view())), #POST calc
    path('api/get-cities', views.get_availible_cities), #GET term
    path('api/put-calc-data', views.PutCalculatorData.as_view()),
    path('api/put-term-data', views.PutTermData.as_view()), 
]

# https://c270-91-219-66-195.ngrok.io/api/put-term-data