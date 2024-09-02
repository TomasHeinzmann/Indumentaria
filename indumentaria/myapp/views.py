from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms
import sqlite3
def shop(request):
    return render(request, "myapp/shop.html")

def contacto(request):
    return render(request, "myapp/contacto.html")

def nueva_remera(request):
    if request.method == "POST":
        form = forms.FormularioRemera(request.POST)
        if form.is_valid():
            conn = sqlite3.connect("db.sqlite3")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO remeras VALUES (?, ?, ?, ?, ?)" , (form.cleaned_data["marca"], form.cleaned_data["talle"], form.cleaned_data["color"], form.cleaned_data["lisa"], form.cleaned_data["genero"]) )
            conn.commit()
            conn.close()
            return HttpResponseRedirect(reverse("shop"))
    else:
        form = forms.FormularioRemera()
    ctx = {"form": form}
    return render(request, "myapp/nueva_remera.html", ctx)