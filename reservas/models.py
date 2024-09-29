from django.db import models



class Horarios(models.Model):
    horarioDeAbertura = models.TimeField()
    horarioDeFechamento = models.TimeField()

    def __str__(self):
        return f"Horario de Abertura: {self.horarioDeAbertura}  Horario de Fechamento: {self.horarioDeFechamento}"
    class Meta:
        verbose_name = 'Horário'
        verbose_name_plural = 'Horários'

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, null=True)

    def __str__(self):
        #senha tem que ver o jeito seguro de armazenar, XD
        return f"Usuário {self.nome } {self.email}  {self.telefone}" 
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    

class Restaurantes(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    capacidadeDeMesas = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"Restaurante {self.nome} {self.endereco} {self.capacidadeDeMesas}"
    #se mudar essa linha aqui, lá no adm a diva muda essa palavra

    class Meta:
        verbose_name = 'Restaurante'
        verbose_name_plural = 'Restaurantes'

    
class Mesa(models.Model):
    restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE)
    numeroDaMesa = models.CharField(max_length=100)
    capacidadeDaMesa = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"Mesa Nº: {self.numeroDaMesa} Capacidade: {self.capacidadeDaMesa}"
    
    class Meta:
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'

class Reserva(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True)
    restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE, null=True, related_name='reservas')

    dataDaReserva = models.DateField()
    horaDaReserva = models.TimeField()
    numero_de_pessoas = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"Reserva para {self.usuario} em {self.dataDaReserva} às {self.horaDaReserva}"
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'





