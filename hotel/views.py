from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import Room, Booking 
from .forms import AvailableForm
from .booking_functions.availability import check_availability

# Create your views here.

class RoomList(ListView):
    model = Room
    
class BookingList(ListView):
    model = Booking
    
class BookingView(FormView):
    form_class = AvailableForm
    template_name = 'available_form.html'
    
    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(categories=data['room_categories'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)