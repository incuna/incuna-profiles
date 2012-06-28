from django.contrib import admin
from django.contrib.admin.options import *
from orderable.admin import OrderableAdmin
from models import *

class SeniorityGroupOptions(OrderableAdmin):
    fields = ('name',)
    search_fields = ('name', )
    ordering = ["sort_order", ] 

class NHSTrustOptions(admin.ModelAdmin):
    fields = ('name', )
    search_fields = ('name', )

class SpecialityOptions(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name', )
    list_display_links = ('name', )
    search_fields = ('name', )

class SubSpecialityOptions(admin.ModelAdmin):
    fields = ('speciality', 'name', )
    list_display = ('name', 'speciality',)
    list_display_links = ('name', )
    search_fields = ( 'name', )
    list_filter = ('speciality', )

class SeniorityOptions(OrderableAdmin):
    fields = ('group', 'name', )
    list_display = ('name', 'group', 'sort_order_display')
    list_display_links = ('name', )
    search_fields = ( 'name', )
    list_filter = ('group', )
    ordering = ["sort_order", ]

admin.site.register(SubSpeciality, SubSpecialityOptions)
admin.site.register(Speciality, SpecialityOptions)
admin.site.register(SeniorityGroup, SeniorityGroupOptions)
admin.site.register(Seniority, SeniorityOptions)
admin.site.register(NHSTrust, NHSTrustOptions)

