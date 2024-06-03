
# tbase/tbase/lk/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ClientRegisterForm
from book.models import Prebook, Clients

def register_user(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        client_form = ClientRegisterForm(request.POST)
        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save()
            client = client_form.save(commit=False)
            client.login = user.username
            client.user = user
            client.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('home')
    else:
        user_form = UserRegisterForm()
        client_form = ClientRegisterForm()
    return render(request, 'authenticate/register.html', {'user_form': user_form, 'client_form': client_form})

@login_required
def user_bookings(request):
    user = request.user
    bookings = Prebook.objects.filter(id_c__login=user.username)
    return render(request, 'lk/user_bookings.html', {'bookings': bookings})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Вы успешно вошли в систему!")
            return redirect('user_bookings')
        else:
            messages.error(request, "Неверное имя пользователя или пароль.")
            return render(request, 'authenticate/log_in.html', {})
    else:
        return render(request, 'authenticate/log_in.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Вы успешно вышли из системы!")
    return redirect('login')