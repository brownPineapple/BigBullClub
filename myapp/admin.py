from django.contrib import admin

# Register your models here.
from .models import Book

from .models import Booking 

admin.site.register(Book)

admin.site.register(Booking)