import json, io
from django.db.models.fields import DecimalField
from django.shortcuts import redirect, render
from order.forms import OrderForm
from calculator.models import Calculate
from django.http import HttpResponse, HttpResponseRedirect
from decimal import Decimal
from django.utils.safestring import SafeString
from consignment.models import OrderConsignment
from loguru import logger


logger.add('logs/debug_order.log', format="{time} {level}, {message}", level="DEBUG", rotation='100 KB')


def order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['date_cargo'] = data['date_cargo'].isoformat()
            for k, v in data.items():
                if isinstance(v, Decimal):
                    data[k] = float(v)
            request.session['contact_form'] = data
            with open('dos.txt', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            logger.info('form has been sent')
            return redirect('confirm_data')
        logger.error('form errors', form.errors)
        print(form.errors)
    form = OrderForm(request.POST or None)
    return render(request, 'order.html', {'form': form})


def confirm_data(request):
    data = request.session['contact_form']
    if request.method == "POST":
        new_order = OrderConsignment(**data)
        new_order.save()
        logger.info('form has been added to database')
        return redirect('thanks')
    return render(request, 'confirm_order.html', {'data': data})


def thanks(request):
    context = {
         'is_worker': request.user.groups.filter(name='worker').exists(),
    }
    return render(request, 'thanks.html', context)
