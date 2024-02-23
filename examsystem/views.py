from django.shortcuts import render


def home(request):
    data = "Welcome to the Store!"
    return render(request, "home.html", context={"data": data})


def aboutus(request):
    data = "About Us page!"
    return render(request, "about.html", context={"data": data})
