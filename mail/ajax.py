from __future__ import unicode_literals
import json

import six
from django.views.generic.base import View
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from mail.models import usages
from mail.models import MailTemplate


class LoadChoices(View):
    def post(self, request, *args, **kwargs):
        department = request.POST["department"]
        used = MailTemplate.objects.values_list('usage', flat=True).filter(department = department)
        valid = {str(x):six.text_type(y) for (x,y) in list(usages.items()) if not any(z in x for z in used)}
        valid.update({'':  '--------'})
        return(HttpResponse(json.dumps(valid), content_type="application/json"))
