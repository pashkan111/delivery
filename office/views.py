from django.views import generic

from office.models import Office

class OfficeList(generic.ListView):
    queryset = Office.objects.all()
    template_name = 'offices.html'
