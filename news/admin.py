from django.contrib import admin
from django import forms
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models

from .models import Post

from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.


class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget}
    }


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(label='Основной текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    form = PostAdminForm
    list_filter = ("status",)
    search_fields = ['title', 'text']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)
