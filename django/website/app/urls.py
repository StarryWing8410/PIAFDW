from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('cajas',views.cajas,name='cajas'),
    path('estanteria',views.estanteria,name='estanteria'),
    path('lockers',views.lockers,name='lockers'),
    path('muebles',views.muebles,name='muebles'),
    path('admin',views.admin,name='admin'),
]