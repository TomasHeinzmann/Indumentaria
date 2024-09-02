from django import forms

class FormularioRemera(forms.Form):
    marca = forms.CharField(label="Marca", max_length=20)
    talles = [
        (1, "XS"),
        (2, "S"),
        (3, "M"),
        (4, "L"),
        (5, "XL"),
        (6, "XXL")
    ]
    talle = forms.ChoiceField(label="Talle", choices=talles)
    color = forms.CharField(label="Color", max_length=30)
    lisa = forms.BooleanField(label="¿Es lisa?", required=True)
    generos = [
        (1, "Hombre"),
        (2, "Mujer"),
        (3, "Unisex")
    ]
    genero = forms.ChoiceField(label="Genero", choices=generos)