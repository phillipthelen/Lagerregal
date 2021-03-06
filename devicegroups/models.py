from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

import six
from reversion import revisions as reversion

from users.models import Department


@six.python_2_unicode_compatible
class Devicegroup(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Devicegroup')
        verbose_name_plural = _('Devicegroups')
        permissions = (
            ("read_devicegroup", _("Can read Devicegroup")),
        )

    def get_absolute_url(self):
        return reverse('devicegroup-detail', kwargs={'pk': self.pk})

    def get_edit_url(self):
        return reverse('devicegroup-edit', kwargs={'pk': self.pk})


reversion.register(Devicegroup)
