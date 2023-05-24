from django import forms

class Login(forms.Form):

    usuario = forms.CharField()
    contrasenia = forms.CharField()

class CrearCuenta(forms.Form):

    usuario = forms.CharField()
    contrasenia = forms.CharField()
    rol = forms.CharField()

class Foda(forms.Form):

    fortaleza = forms.CharField()
    oportunidad = forms.CharField()
    debilidad = forms.CharField()
    amenaza = forms.CharField()

class Mensaje(forms.Form):

    mensaje = forms.CharField()
