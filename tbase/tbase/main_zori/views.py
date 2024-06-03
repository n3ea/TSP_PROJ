
#tbase/tbase/main_zori/views.py
#вывод на экран пользователя?

from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'main_zori/design.html')

def about(request):
    return render(request, 'main_zori/about.html')

def booking(request):
    return render(request, 'book/book_home.html')

def serv(request):
    return render(request, 'book/book_serv.html')

def lk(request):
    return render(request, 'authenticate/log_in.html')

