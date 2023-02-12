from django.shortcuts import render

from django.http import HttpResponse

from .models import Book
from .models import Booking
# Create your views here.

def index(request):
    return HttpResponse("Hello World !")

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book':book})
    # return HttpResponse(f"Book: {book.title}, published on {book.pub_date}")

def booking_by_id(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    return render(request, 'booking_details.html', {'booking':booking})

def booking_list(request, booking_list):
    booking1 = Booking.objects.get(pk=booking_list)
    for x in range(booking_list):
        personName = booking_list[x]
        return HttpResponse(f"Booking: {booking1.personName}")