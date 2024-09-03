from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms
from .models import Remera

def shop(request):
    remeras = Remera.objects.all()
    ctx = {"remeras":remeras}
    return render(request, "myapp/shop.html", ctx)

def contacto(request):
    return render(request, "myapp/contacto.html")

def nueva_remera(request):
    if request.method == "POST":
        form = forms.FormularioRemera(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("shop"))
    else:
        form = forms.FormularioRemera()
    ctx = {"form": form}
    return render(request, "myapp/nueva_remera.html", ctx)