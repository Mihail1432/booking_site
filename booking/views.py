from django.shortcuts import render
from booking.models import Room, Booking

# Create your views here.
def room_list(request):
    rooms = Room.objects.all()

    context = {
        "room_list": rooms
    }

    return render(request, "booking/room_list.html", context=context)

def room_details(request, room_id):
    room = Room.objects.get(id=room_id)
    bookings = Booking.objects.filter(room_id = room_id)

    context = {
        "room": room,
        "bookings": bookings
    }

    return render(request, "booking/room_details.html", context=context)

