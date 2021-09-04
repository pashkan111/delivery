from django.urls import path
from tracking import views
# from tracking.views import Search

urlpatterns = [
    path('search/', views.Search.as_view(), name='search'),
    path('api/consignment_create_track', views.create_consignment_trackstatus), #POST track
    path('api/consignment_track/<str:pk>', views.consignment_detail_trackstatus),
    path('api/get-track-info/', views.Trak.as_view()),
]