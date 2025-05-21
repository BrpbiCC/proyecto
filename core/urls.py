from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('registro/', registro, name='registro'),
    path('login/', login, name='login'),
    path('hospedaje/', hospedaje, name='hospedaje'),
    path('actividad/', actividad, name='actividad'),
    path('gastronomia/', gastronomia, name='gastronomia'),
    path('carrito/', carrito, name='carrito'),
]