from django.contrib import admin
from .models import Reserva, Mesa, Horarios, Restaurantes, Usuarios

# Register your models here.
admin.site.register(Reserva)
admin.site.register(Mesa)
admin.site.register(Horarios)
admin.site.register(Usuarios)

class ReservaInline(admin.TabularInline):
    model = Reserva
    extra = 1

class RestauranteAdmin(admin.ModelAdmin):
    inlines = [ReservaInline]

admin.site.register(Restaurantes, RestauranteAdmin)