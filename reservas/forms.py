from django import forms
from .models import Usuarios, Reserva, Mesa, Horarios, Restaurantes

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['mesa', 'usuario', 'restaurante', 'dataDaReserva', 'horaDaReserva', 'numero_de_pessoas']
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nome', 'email', 'senha', 'telefone']


class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurantes
        fields = ['nome', 'endereco', 'capacidadeDeMesas']

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['restaurante', 'numeroDaMesa', 'capacidadeDaMesa']

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horarios
        fields = ['horarioDeAbertura', 'horarioDeFechamento']