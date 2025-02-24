from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone  # اضافه کردن این خط
from datetime import timedelta  # اضافه کردن این خط

from django.utils import timezone
from django.core.exceptions import ValidationError


from django.db import models
from django.utils.translation import gettext as _

class Reservation(models.Model):
    NUMBER_OF_PEOPLE_CHOICES = [
        (1, _('1 نفر')),
        (2, _('2 نفر')),
        (3, _('3 نفر')),
        (4, _('4 نفر')),
    ]

    name = models.CharField(_('نام کامل'), max_length=100)
    email = models.EmailField(_('ایمیل'))
    phone = models.CharField(_('تلفن'), max_length=15)
    number_of_people = models.PositiveSmallIntegerField(
        _('تعداد افراد'),
        choices=NUMBER_OF_PEOPLE_CHOICES,
        default=2
    )
    date = models.DateField(_('تاریخ'))
    time = models.TimeField(_('زمان'))
    special_request = models.TextField(_('درخواست ویژه'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(
        _('تایید شده'),
        default=False
    )

    def __str__(self):
        return f"{self.name} - {self.date}"