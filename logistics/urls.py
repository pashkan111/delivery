from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
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
    path('', include('tracking.urls')),
    path('', include('news.urls')),
    path('', include('office.urls')),
    path('', include('accounts.urls')),
    path('', include('calculator.urls')),
    path('', include('order.urls')),
    path('tracking/', include('tracking.urls'), name='tracking'),
    path('', include('consignment.urls')),

    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
