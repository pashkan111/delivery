import json

from django.shortcuts import redirect, render

from order.forms import OrderForm

from calculator.models import Calculate

# Create your views here.


def order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    return render(request, 'order.html', {'form': form})


def thanks(request):
    context = {
         'is_worker': request.user.groups.filter(name='worker').exists(),
    }
    return render(request, 'thanks.html', context)


def my_data(request):
    data = json.loads(request.body)
    max_weight = max(data[2], data[3]*240)
    response = Calculate.objects.filter(cityto__exact=data[0]).filter(cityfrom__exact=data[1]).filter(weightto__gte=max_weight).filter(weightfrom__lte=max_weight)
    res_order = {
        'my_data': response
    }
    return json.dumps(res_order)
