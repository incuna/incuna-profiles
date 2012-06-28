from django.contrib import admin
from orderable.admin import OrderableAdmin
from .models import Opportunity


class OptionOptions(OrderableAdmin):
    fields = ('name',)
    search_fields = ('name',)
    ordering = ['sort_order']

admin.site.register(Opportunity, OptionOptions)
