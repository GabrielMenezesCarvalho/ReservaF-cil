from django.shortcuts import render, redirect
from .forms import ReservaForm

def nova_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacao')
    else:
        form = ReservaForm()
    return render(request, 'reservas/nova_reserva.html', {'form': form})

def confirmacao(request):
    return render(request, 'reservas/confirmacao.html')
