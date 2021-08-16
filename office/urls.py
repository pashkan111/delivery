from django.urls import path

from . import views

urlpatterns = [
    path('offices/', views.OfficeList.as_view(), name='offices'),
]