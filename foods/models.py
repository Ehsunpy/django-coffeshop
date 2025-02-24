from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Foods(models.Model):
    name = models.CharField(_('نام'),max_length=100)
    description = models.CharField(_("توضیحات"),max_length=200)
    rate = models.IntegerField(_("امتیاز"),default=0)
    price = models.IntegerField(_('قیمت'))
    pub_data = models.DateField(_("تاریخ انتشار"), auto_now=False,auto_now_add=True)
    time  = models.IntegerField(_("زمان لازم"))
    photo = models.ImageField(upload_to='foods/')
    category = models.CharField(max_length=10, choices=[('hot', 'Hot'), ('cold', 'Cold')], default='hot')
    def __str__(self):
        return self.name