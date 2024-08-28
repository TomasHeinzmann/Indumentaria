from django.shortcuts import render, HttpResponse

def shop(request):
    return render(request, "myapp/shop.html")

def contacto(request):
    return render(request, "myapp/contacto.html")