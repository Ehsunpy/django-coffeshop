# forms.py
from django import forms
from django.utils.translation import gettext as _
from .models import Foods  # Import your Foods model

class FoodsForm(forms.ModelForm):
    class Meta:
        model = Foods
        fields = '__all__'  # Include all model fields
        labels = {
            'name': _('نام'),  # Set labels, including translated ones
        }