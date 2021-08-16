from django.urls import path

from order.views import order, thanks

urlpatterns = [
    path('order/', order, name='order'),
    path('thanks/', thanks, name='thanks'),
]