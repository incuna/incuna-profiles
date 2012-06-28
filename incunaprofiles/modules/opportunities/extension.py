from django.db import models
from django.utils.translation import ugettext_lazy as _

def register(cls, admin_cls):
    cls.add_to_class('opportunities', models.ManyToManyField('profiles.Opportunity', verbose_name=_('Commercial opportunities'), null=True, blank=True))

    if admin_cls:
        admin_cls.list_display_filter += ['opportunities', ]

        if admin_cls.fieldsets:
            admin_cls.fieldsets.append((_('Commercial opportunities'), {
                    'fields': ['opportunities',],
                    'classes': ('collapse',),
                }))
            admin_cls.filter_horizontal = admin_cls.filter_horizontal + ('opportunities',)
