from django.urls import path

from . import views

urlpatterns = [
    path('offices/', views.OfficeView.as_view(), name='offices'),
]