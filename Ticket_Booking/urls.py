from django.contrib import admin
from django.urls import path, re_path, include
from Ticket_Booking import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^Booking', views.Booking, name='Booking'),
    re_path(r'^ticket_finalised', views.ticket_finalised, name='ticket_finalised'),
]
