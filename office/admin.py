# from django.contrib import admin
# from django import forms
# from django.contrib.flatpages.admin import FlatPageAdmin
# from django.contrib.flatpages.models import FlatPage
# from django.db import models

# from .models import Office

# from ckeditor_uploader.widgets import CKEditorUploadingWidget
# # Register your models here.


# class FlatPageCustom(FlatPageAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': CKEditorUploadingWidget}
#     }


# class OfficeAdminForm(forms.ModelForm):
#     city = forms.CharField(label='Город', widget=CKEditorUploadingWidget())
#     text = forms.CharField(label='Основной текст', widget=CKEditorUploadingWidget())

#     class Meta:
#         model = Office
#         fields = '__all__'


# class OfficeAdmin(admin.ModelAdmin):
#     list_display = ('city', 'text')
#     form = OfficeAdminForm
#     list_filter = ("city",)
#     search_fields = ['city', 'text']


# admin.site.register(Office, OfficeAdmin)
# admin.site.unregister(FlatPage)
# admin.site.register(FlatPage, FlatPageCustom)
