
#tbase/tbase/book/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('book_home', views.book_home, name = 'book_home'),
    path('serv', views.book_serv, name = 'book_serv'),
    path('create', views.create_booking, name ='create'),
    path('free_rooms', views.free_rooms, name ='free_rooms')
    #path("postdate/", views.postdate)
]