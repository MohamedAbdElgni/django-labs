from django.shortcuts import render


def home(request):
    data = "Welcome to the Examsystem"
    return render(request, 'home.html' , context={'data':data})