from django.urls import path
from . import views
urlpatterns = [
    path('', views.booking_view, name='booking_form'),
    path('success/', views.booking_success, name='booking_success'),
]
