from django.urls import path

from common.views import landing_page, tracking_page, page_404, price_page, reglog, db



urlpatterns = [
    path('', landing_page, name='index'),
    path('tracking/', tracking_page, name='tracking'),
    path('price/', price_page, name='price'),
    path('reglog/', reglog, name='reglog'),
    path('page_404/', page_404, name='page_404'),
    path('db/', db, name='db'),
]