

from django.urls import path
from . import views

app_name = 'reservation'  # حذف این خط یا اصلاح استفاده از namespace

urlpatterns = [
    path('', views.SimpleReservationView.as_view(), name='reserve'),
    path('success/', views.ReservationSuccessView.as_view(), name='reservation_success'),
    path('list-reserve',views.ShoweReservationView.as_view(),name='list-reserve'),

]