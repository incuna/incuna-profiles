from django.db import models
from django.utils.safestring import mark_safe
from orderable.models import Orderable


class Opportunity(Orderable):
    name = models.CharField(max_length=150)

    class Meta:
        app_label = 'profiles'
        ordering = ('sort_order',)
        verbose_name_plural = 'Opportunities'

    def __unicode__(self):
        return mark_safe(self.name)
