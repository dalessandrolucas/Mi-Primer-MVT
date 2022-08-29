from django.shortcuts import render
from AppProyecto.models import Familiar
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def familiar_uno(request):
    familiar1= Familiar(nombre="Franco", edad=14, fecha_nacimiento=2008/4/22)
    familiar1.save()
    diccionario= {f"Familiar registrado, {familiar1.datos}"}
    plantilla= loader.get_template('template1.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)
