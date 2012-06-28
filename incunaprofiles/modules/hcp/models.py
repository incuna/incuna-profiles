from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.db import models
from orderable.models import Orderable


class SeniorityGroup(Orderable):
    name = models.CharField(max_length=150)

    class Meta:
        app_label = 'profiles'
        ordering = ('sort_order', )

    def __unicode__(self):
        return self.name

class Seniority(Orderable):
    group = models.ForeignKey('profiles.SeniorityGroup', related_name='seniorities')
    name = models.CharField(max_length=150)

    class Meta:
        app_label = 'profiles'
        verbose_name_plural = 'seniorities'
        ordering = ('sort_order', )
        unique_together = (('group', 'sort_order'),)

    def __unicode__(self):
        return self.name

class Speciality(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        app_label = 'profiles'
        verbose_name_plural = 'specialities'
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class SubSpeciality(models.Model):
    speciality = models.ForeignKey('profiles.Speciality')
    name = models.CharField(max_length=150)

    class Meta:
        app_label = 'profiles'
        verbose_name_plural = 'sub specialities'
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class NHSTrust(models.Model):
    name = models.CharField(max_length=150)
   
    class Meta:
        app_label = 'profiles'
        ordering = ('name',)
        verbose_name = 'NHS Trust'
   
    def __unicode__(self):
        return self.name

