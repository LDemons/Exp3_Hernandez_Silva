from django.urls import path
from .views import p_inicio, Sobre_Nosotros, Ventas, Adopcion, Calculadora, crear, modificar, registrar,  eliminar, mostrar

urlpatterns=[ 
    path('', p_inicio, name="p_inicio"),
    path('Sobre_Nosotros/',Sobre_Nosotros, name="Sobre_Nosotros"),
    path('Ventas/',Ventas, name="Ventas"),
    path('Adopcion/',Adopcion, name="Adopcion"),
    path('Calculadora/',Calculadora, name="Calculadora"),
    path('crear/', crear, name="crear"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/', registrar, name="registrar"),
    path('mostrar/', mostrar, name="mostrar"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    #
]