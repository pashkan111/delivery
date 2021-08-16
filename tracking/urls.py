from django.urls import path

from tracking.views import Search

urlpatterns = [
    path('search/', Search.as_view(), name='search'),
]