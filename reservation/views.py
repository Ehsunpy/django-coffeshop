from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm
from django.utils import timezone  # اضافه کردن این خط
from datetime import timedelta  # اضافه کردن این خط

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import Reservation
from .forms import ReservationForm

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Reservation
from django.views.generic import TemplateView

class ReservationSuccessView(TemplateView):
    template_name = 'reservation/reservation_success.html'

class SimpleReservationView(CreateView):
    model = Reservation
    fields = '__all__'
    template_name = 'reservation/reservation.html'
    success_url = reverse_lazy('reservation:reservation_success')