from django.core.management.base import BaseCommand
import random
from faker import Faker
from reservas.models import Usuarios, Restaurantes, Mesa, Reserva, Horarios

# Criando o objeto Faker com a localização para o Brasil
fake = Faker('pt_BR')

# Funções para popular o banco de dados
def criar_usuarios(n):
    for _ in range(n):
        Usuarios.objects.create(
            nome=fake.name(),
            email=fake.email(),
            senha=fake.password(),
            telefone=fake.cellphone_number()  # Sem código de país
        )

def criar_restaurantes(n):
    for _ in range(n):
        Restaurantes.objects.create(
            nome=fake.company(),
            endereco=fake.address(),
            capacidadeDeMesas=random.randint(8, 30)  # Entre 10 e 50 mesas
        )

def criar_mesas(n):
    restaurantes = Restaurantes.objects.all()
    for restaurante in restaurantes:
        for _ in range(n):
            Mesa.objects.create(
                restaurante=restaurante,
                numeroDaMesa=str(random.randint(1, 100)),
                capacidadeDaMesa=random.randint(2, 8)  # Mesas para 2 a 10 pessoas
            )

def criar_reservas(n):
    usuarios = Usuarios.objects.all()
    mesas = Mesa.objects.all()
    for _ in range(n):
        Reserva.objects.create(
            mesa=random.choice(mesas),
            usuario=random.choice(usuarios),
            restaurante=random.choice(Restaurantes.objects.all()),
            dataDaReserva=fake.date_this_year(),
            horaDaReserva=fake.time(),
            numero_de_pessoas=random.randint(1, 10)
        )

def criar_horarios(n):
    for _ in range(n):
        Horarios.objects.create(
            horarioDeAbertura=fake.time(),
            horarioDeFechamento=fake.time()
        )

# Classe que define o comando personalizado
class Command(BaseCommand):
    help = 'Popula o banco de dados com dados falsos'

    def handle(self, *args, **kwargs):
        criar_usuarios(10)  # Cria 10 usuários
        criar_restaurantes(5)  # Cria 5 restaurantes
        criar_mesas(10)  # Cria 10 mesas por restaurante
        criar_reservas(20)  # Cria 20 reservas
        criar_horarios(5)  # Cria 5 horários
        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
