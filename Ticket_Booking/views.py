from django.shortcuts import render
from django.http import HttpResponse
from Ticket_Booking.models import Ticket_Details
# Create your views here.

def home(Request):
    # return HttpResponse("This is my home page")
    return render(Request, 'Ticket_Booking/home.html')

def Booking(Request):
    # return HttpResponse("This is my booking page")
    return render(Request, 'Ticket_Booking/Booking.html')

def ticket_finalised(Request):
    # return HttpResponse("This is my Ticket_Finalised page")
    ticket_mdl_details = Ticket_Details.objects.order_by("IRCTC_ID")
    ticket_details_dict = {"insert_ticket_details": ticket_mdl_details}

    return render(Request, 'Ticket_Booking/ticket_finalised.html', context=ticket_details_dict )


