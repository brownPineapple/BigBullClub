from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>', views.book_by_id, name='book_by_id'),
    path('booking/list', views.booking_list, name='booking_list'),
    path('booking/<int:booking_id>', views.booking_by_id, name='booking_by_id'),
]