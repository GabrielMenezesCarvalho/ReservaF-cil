from django.contrib import admin
from .models import Reserva, Mesa, Horarios, Restaurantes, Usuarios

# Register your models here.
admin.site.register(Reserva)
admin.site.register(Mesa)
admin.site.register(Horarios)
admin.site.register(Restaurantes)
admin.site.register(Usuarios)

