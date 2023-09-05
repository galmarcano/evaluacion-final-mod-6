from django.shortcuts import render, redirect
from vehiculo.models import VehiculoForm
from django.contrib import messages
from vehiculo.models import Vehiculo
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def v_index(request):
    context = {

    }
    return render(request, 'index.html', context)

@permission_required('your_app.add_vehiculo')
def ingresar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo agregado exitosamente.')  # Agregar mensaje de éxito
            return redirect('ingresar_vehiculo')  # Redirigir al formulario de ingreso nuevamente
        else:
            messages.error(request, 'Hubo un error en el formulario. Por favor, verifica los datos.')  # Agregar mensaje de error si el formulario no es válido
    else:
        form = VehiculoForm()
    return render(request, 'form_vehiculos.html', {'form': form})

@login_required
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'listar_vehiculos.html', {'vehiculos': vehiculos})