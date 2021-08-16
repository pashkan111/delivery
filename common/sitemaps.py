from django.contrib.sitemaps import Sitemap
from django.contrib.flatpages.models import FlatPage
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ['tracking']

    def location(self, item):
        return reverse(item)


class FlatPageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return FlatPage.objects.all()

