from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    path('', registro, name='registro'),
    path('', login, name='login'),
    path('', hospedaje, name='hospedaje'),
    path('', actividad, name='actividad'),
    path('', gastronomia, name='gastronomia'),

]