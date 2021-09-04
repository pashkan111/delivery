from django.contrib import admin
from .models import *


class AdminCalc(admin.ModelAdmin):
    fields = ('cityfrom', 'cityto','inter_terminal',)
    
admin.site.register(City)
admin.site.register(Calculate, AdminCalc)
admin.site.register(Term)