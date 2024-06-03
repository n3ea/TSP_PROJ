from django.db.models import Subquery
#tbase/tbase/book/views.py
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room_Info, Serv_Info, Prebook, Clients
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from django.http import JsonResponse


def free_rooms(request):
    b_start = request.GET['b_start']
    b_end = request.GET['b_end']
    rooms = show_fr(b_start, b_end)
    return render(request, 'book/free_rooms.html', {'rooms': rooms})

def book_serv(request):
    all_serv = view_all(Serv_Info)
    return render(request, 'book/book_serv.html', {'all_serv': all_serv})

def book_home(request):
    all_houses = view_all(Room_Info)
    return render(request, 'book/book_home.html', {'all_houses': all_houses})

def view_all(model):
    return model.objects.all()

def show_fr(date1, date2):
    mas=[]
    free_rooms = Room_Info.objects.raw("SELECT * FROM book_room_info WHERE id=6 or id not IN (SELECT room_info_id FROM book_prebook_room_nums JOIN book_prebook ON book_prebook_room_nums.prebook_id=book_prebook.id_req WHERE ((b_start between %s and %s) or (b_end between %s and %s)))", [date1, date2, date1, date2])
    # for room in free_rooms:
    #     mas.append(room.title)
    return(free_rooms)
    # reservations = Prebook.objects.filter(Q(b_start__range=(date1, date2)) | Q(b_end__range=(date1, date2))).values(
    #     'room_nums')
    # queryset = Room_Info.objects.exclude(id__in=reservations)
    # return queryset

def show_fs(date1, date2):
    mas=[]
    free_serv = Serv_Info.objects.raw("select * from book_serv_info where id=4 or id not in (select serv_info_id from book_prebook_serv_n join book_prebook ON book_prebook_serv_n.prebook_id=book_prebook.id_req WHERE ((b_start between %s and %s) or (b_end between %s and %s)))", [date1, date2, date1, date2])
    for serv in free_serv:
        mas.append(serv.serv_name)
    return (mas)

@login_required
def create_booking(request):
    try:
        client = Clients.objects.get(user=request.user)
    except Clients.DoesNotExist:
        messages.error(request, "Не удалось найти клиента для текущего пользователя.")
        return redirect('home')  # Или на другую подходящую страницу

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.id_c = client  # Привязываем объект клиента
            booking.save()
            form.save_m2m()  # Сохраняем многие-ко-многим данные для формы
            messages.success(request, "Бронь успешно создана!")
            return redirect('user_bookings')
        else:
            messages.error(request, "Произошла ошибка при создании брони. Пожалуйста, проверьте введенные данные.")
    else:
        form = BookingForm()

    return render(request, 'book/create.html', {'form': form})



def delete_prebook(id):
    del_prb = Prebook.objects.get(id_req=id)
    del_prb.delete()

def cancel_book(id):
    upd_prb = Prebook.objects.get(id_req=id)
    upd_prb.stat = 3
    upd_prb.save()
    print('Бронь отменена')

def confirm_book(id):
    upd_prb = Prebook.objects.get(id_req=id)
    upd_prb.stat = 2
    upd_prb.save()
    print('Бронь подтверждена')

def show_all_books(id_c):
    mas1=[]
    mas2=[]
    all_books = Prebook.objects.filter(id_c=id_c)
    for el in all_books:
        print()
        print('ID брони:  ', el.id_req)
        rns = Room_Info.objects.raw('select * from book_room_info where id in (select room_info_id from book_prebook_room_nums where prebook_id=%s)', [el.id_req])
        for room in rns:
            mas1.append(room.title)
        print('Дома:   ', mas1)
        sns=Serv_Info.objects.raw('select * from book_serv_info where id in (select serv_info_id from book_prebook_serv_n where prebook_id=%s)', [el.id_req])
        for serv in sns:
            mas2.append(serv.serv_name)
        print('Услуги:   ', mas2)
        print('Дата заезда:   ', el.b_start)
        print('Дата выезда:   ', el.b_end)
        print('Статус брони:   ', el.get_stat_display())

def create_user(login, password):
    mass=[]
    cls = Clients.objects.all()
    for el in cls:
        mass.append(el.login)
    if login in mass:
        print('Пользователь с таким логином уже существует')
    else:
        print('Пользователь создан')


def update_user(id,fio, tel, mail):
    Clients.objects.filter(id_cl = id).update(fio=fio, tel_n=tel, e_mail=mail)
    print('Профиль отредактирован')


def delete_user(id):
    del_us = Clients.objects.get(id_cl=id)
    del_us.delete()
    print('Пользователь ', id, ' удален')

print(show_fr('2024-05-16', '2024-05-17'))
b_start = '2024-05-14'
b_end = '2024-05-15'
reservations = Prebook.objects.filter( Q(b_start__range=(b_start, b_end)) | Q(b_end__range=(b_start, b_end))).values('room_nums')
rooms = Room_Info.objects.filter(Q(id=6) | ~Q(id__in=reservations))
#print(rooms)