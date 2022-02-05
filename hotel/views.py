from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import Room, Booking 
from .forms import AvailableForm

# Create your views here.

class RoomList(ListView):
    model = Room
    
class BookingList(ListView):
    model = Booking
    
class BookingView(FormView):
    form_class = AvailableForm