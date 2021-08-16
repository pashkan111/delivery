from django.urls import path, re_path

from calculator.views import calc
from calculator import views

urlpatterns = [
    path('calc/', calc, name='calc'),
    path('api/create_calc', views.create_calculate), #POST calc
    re_path('api/calc/(?P<pk>[0-9]+)', views.update_calculate), #PUT calc
    path('api/create_term', views.create_term), #POST term
    path('api/get-cities', views.get_availible_countries), #GET term
    re_path('api/term/(?P<pk>[0-9]+)', views.update_term), #PUT term
    
]