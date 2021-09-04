from django.urls import path

from order.views import order, thanks, confirm_data

urlpatterns = [
    path('order/', order, name='order'),
    path('confirm_data/', confirm_data, name='confirm_data'),
    path('thanks/', thanks, name='thanks'),
]