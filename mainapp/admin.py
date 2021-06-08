from django import forms
from django.contrib import admin
from .models import *


class GoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title')


class ThingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title')


class NoteBookAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return forms.ModelChoiceField(ProdCategories.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return forms.ModelChoiceField(ProdCategories.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Good)
admin.site.register(Things)
admin.site.register(BlogCategory)
admin.site.register(BlogPost)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(ProdCategories)
admin.site.register(Customer)
admin.site.register(Notebook, NoteBookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Order)
