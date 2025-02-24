from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Reservation
from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'is_confirmed')
    list_filter = ('date', 'is_confirmed')  # حالا is_confirmed یک فیلد معتبر است
    search_fields = ('name', 'phone', 'email')