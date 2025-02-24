from django.urls import path
from . import views

app_name = "foods"  # Namespace برای مسیرها

urlpatterns = [
    path("", views.food_list, name='food_list'),  # مسیر اصلی برای لیست غذاها
    path('<int:pk>/', views.food_detail, name='food_detail'),  # مسیر برای جزئیات غذا با id مشخص
    # path('eee/', views.food_detail, name=   'food'),

]