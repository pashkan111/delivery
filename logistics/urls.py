"""logistics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import contrib
from django import urls
from django.contrib import admin
from django.contrib.admin.sites import site
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  include
from django.contrib.sitemaps.views import sitemap

from common.sitemaps import FlatPageSitemap, StaticViewSitemap



sitemaps = {
    'flatpages': FlatPageSitemap,
    'static': StaticViewSitemap,
}

admin.site.index_template = 'admin/custom_index.html'
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('common.urls')),
    path('', include('news.urls')),
    path('', include('office.urls')),
    path('', include('accounts.urls')),
    path('', include('calculator.urls')),
    path('', include('order.urls')),
    path('tracking/', include('tracking.urls'), name='tracking'),
    path('', include('consignment.urls')),

    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
