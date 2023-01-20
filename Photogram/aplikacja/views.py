from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'nickname': 'martunia880',
        'photo': 'example photo',
        'content': 'My irst post',
        'date': '23/02/2022'
    },
    {
        'nickname': 'dejwero',
        'photo': 'examle photo',
        'content': 'First post',
        'date': '21/02/2022'
    }
]

def photogram(request):
    return render(request, 'photogram.html', {'title': 'Witamy!'})
def mainpage(request):
    context = {
        'posts': posts
    }
    return render(request, 'mainpage.html', context, {'title': 'Strona główna'})
def login(request):
    return render(request, 'login.html', {'title': 'Zaloguj się'})
def signup(request):
    return render(request, 'signup.html', {'title': 'Zarejestruj się'})
def profile(request):
    return render(request, 'profile.html', {'title': 'Twój profil'})