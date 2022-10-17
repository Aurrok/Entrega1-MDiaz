from familia import views
from django.urls import path


urlpatterns = [
    path('' , views.indice, name= 'indice'),
    path("personas/", views.hola),
    path("fecha-nacimiento/<int:edad>" , views.calcular_fecha),
    path("mi-template/", views.mi_template),
    path("mi-template/<str:nombre>", views.mi_template),
    path("prueba",views.prueba),
    path("crear-persona/", views.crear_persona, name = 'crear_persona'),
    path("ver-familiares/" , views.ver_familiares, name = 'familiares'),
    
    
]