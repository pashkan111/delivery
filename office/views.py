from django.views import generic
from office.models import City, Office


class OfficeView(generic.ListView):
    template_name = 'test.html'
    queryset = Office.objects.all().select_related('city')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['offices'] = self.queryset
        data['cities'] = City.objects.all()
        return data


        


