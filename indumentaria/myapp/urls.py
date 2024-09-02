from django.urls import path
from . import views
urlpatterns = [
    path("shop/", views.shop, name="shop"),
    path("contacto/", views.contacto, name="contacto"),
    path("nueva_remera/", views.nueva_remera, name="nueva_remera")
]