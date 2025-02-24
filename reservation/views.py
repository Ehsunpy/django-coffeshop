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

from django.views.generic import CreateView,DetailView , ListView
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

class ShoweReservationView(ListView):
    model = Reservation
    template_name = 'reservation/showreserve.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        queryset = super().get_queryset()

        # دریافت پارامترهای فیلتر از URL
        date = self.request.GET.get('date')
        number_of_people = self.request.GET.get('number_of_people')

        # اعمال فیلتر بر اساس تاریخ
        if date:
            queryset = queryset.filter(date=date)

        # اعمال فیلتر بر اساس تعداد نفرات
        if number_of_people:
            queryset = queryset.filter(number_of_people=number_of_people)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # افزودن پارامترهای فیلتر به context برای استفاده در تمپلیت
        context['current_date'] = self.request.GET.get('date', '')
        context['current_number'] = self.request.GET.get('number_of_people', '')

        return context