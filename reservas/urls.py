from django.urls import path
from . import views

urlpatterns = [
    path('', views.nova_reserva, name='nova_reserva'),
    path('confirmacao/', views.confirmacao, name='confirmacao'),
]
