from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect


def photogram(request):
    return render(request, 'photogram.html', {'title': 'Witamy!'})
def mainpage(request):
    return render(request, 'mainpage.html', {'title': 'Strona główna'})
def login(request):
    return render(request, 'login.html', {'title': 'Zaloguj się'})
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'E-mail zajęty')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Nazwa użytkownika zajęta')
                return redirect('signup')
            else:
                user = User.objects.create_user()
        else:
            messages.info(request, 'Wpisane hasła różnią się od siebie')
            return redirect('signup')
    else:
        return render(request, 'signup.html', {'title': 'Zarejestruj się'})
def profile(request):
    return render(request, 'profile.html', {'title': 'Twój profil'})