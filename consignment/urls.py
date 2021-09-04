from django.urls import path, re_path

from consignment import views


urlpatterns = [
     path('api/consignment', views.consignment_list_order), #GET, DELETE order
    path('api/consignment_create_order', views.create_consignment_orderstatus), #POST order
    re_path('api/consignment_order/(?P<pk>[0-9]+)', views.consignment_detail_orderstatus), #PUT order
    path('api/add_cities', views.add_cities),
]