from django.urls import path
from .views import RoomListView, BookingList, RoomDetailView, CancelBookingView

app_name ='hotel'

urlpatterns =[
    path('room_list/', RoomListView, name='RoomList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(), name='CancelBookingView'),
    path('room/<category>/', RoomDetailView.as_view(), name='RoomDetailView'),
]