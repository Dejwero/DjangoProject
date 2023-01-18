from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def photogram(request):
    return render(request, 'photogram.html')
def mainpage(request):
    return render(request, 'mainpage.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
def profile(request):
    return render(request, 'profile.html')