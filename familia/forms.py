from django import forms


class FamiliarFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha = forms.DateField(required=False)
class BuFamiliarFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
