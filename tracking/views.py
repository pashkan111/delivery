from django.shortcuts import render
from django.views.generic.list import ListView

from consignment.models import TrackStatusConsignment

# Create your views here.

class Search(ListView):
    model = TrackStatusConsignment()
    template_name = 'tracking.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = TrackStatusConsignment.objects.filter(tracking_number__icontains=query)

        return object_list