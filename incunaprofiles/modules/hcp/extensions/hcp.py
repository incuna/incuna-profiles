from django.db import models
from django.utils.translation import ugettext_lazy as _
from incuna.utils import find

def register(cls, admin_cls):
    cls.add_to_class('gmc_number', models.CharField(max_length=15, verbose_name=_('GMC/NMC Number'), null=True, blank=True))
    cls.add_to_class('seniority', models.ForeignKey('profiles.Seniority', null=True))
    cls.add_to_class('speciality', models.ForeignKey('profiles.Speciality', null=True))
    cls.add_to_class('sub_specialities', models.ManyToManyField('profiles.SubSpeciality', null=True, blank=True))
    # address
    cls.add_to_class('surgery', models.CharField(max_length=255, verbose_name=_('Practice name'), null=True))
    cls.add_to_class('nhs_trust', models.ForeignKey('profiles.NHSTrust', verbose_name=_('NHS Trust'), null=True, blank=True))

    if admin_cls:
        admin_cls.search_fields += ['gmc_number', 'surgery']
        admin_cls.list_display_filter += ['seniority', 'speciality', 'sub_specialities', 'nhs_trust']

        if admin_cls.fieldsets:
            fields = admin_cls.fieldsets[0][1]['fields']
            try:
                at = fields.index('last_name') + 1
            except ValueError:
                at = len(fields)
            fields[at:at] = ['gmc_number', 'speciality', 'sub_specialities']
            admin_cls.filter_horizontal += ('sub_specialities',)

            address_title = _('Address')

            address_set =  find(lambda sets: sets[0] == address_title, admin_cls.fieldsets)

            if address_set:
                address_fields = address_set[1]['fields'] 
                address_fields.insert(0, 'surgery')
                try:
                    at = address_fields.index('postcode') + 1
                except ValueError:
                    at = len(address_fields)
                address_fields.insert(at, 'nhs_trust')
            else:
                at = len(fields)
                fields[at:at] = ['surgery', 'nhs_trust']
