from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template , loader
import random
from familia.models import Familiar
from django.shortcuts import render
from familia.forms import FamiliarFormulario

# from symbol import return_stmt



def hola(request):
    return HttpResponse("Buenas Clase ")

def calcular_fecha(request, edad):
    fecha = datetime.now().year -edad  #datetime.now().year - edad
    return HttpResponse(f"la edad es {edad} y la fecha es : {fecha}")

def mi_template(request, nombre):
    # cargar_archivo = open(r"D:\segundo intento\proyecto\templates\template.html", "r")
    
    # template = Template(cargar_archivo.read())
    
    # cargar_archivo.close()
    
    # contexto = Context({"persona": nombre})
    
    # template_renderizado = template.render(contexto)
    template = loader.get_template("template.html")
    
    template_renderizado = template.render({"persona" : nombre})
    
    return HttpResponse(template_renderizado)

def prueba(request):
    mi_contexto ={"rango": list(range(1,11))}
    template = loader.get_template("template_lista.html")
    template_rendizado =template.render(mi_contexto)
    return HttpResponse(template_rendizado)



def crear_persona(request):
    # personas.save()
    # template = loader.get_template("crear_familiar.html")
    # template_renderizado = template.render({"personas: " : personas})
    if request.method == 'POST':
        formulario = FamiliarFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha = data.get('fecha',datetime.now())
            
            persona = Familiar(nombre=nombre , apellido=apellido , edad = edad, fecha= fecha)
            persona.save()
        # return HttpResponse(template_renderizado)
    formulario = FamiliarFormulario()
    return render(request,'crear_familiar.html',{'formulario': formulario})

def ver_familiares(request):
    
    personas = Familiar.objects.all() 
    
    # template = loader.get_template("ver_familiares.html")
    # template_renderizado = template.render( {"personas" : personas})
    # return HttpResponse(template_renderizado)
    return render(request,"ver_familiares.html" , {"personas" : personas})

def indice(request):    
    
    return render(request, 'index.html')
    
    
    