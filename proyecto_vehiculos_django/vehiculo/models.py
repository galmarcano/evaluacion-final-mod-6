from django.db import models
from django import forms

# Create your models here.

class Vehiculo(models.Model):
    MARCA_CHOICES = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]

    CATEGORIA_CHOICES = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]

    marca = models.CharField(max_length=20, choices=MARCA_CHOICES, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='Particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    condicion_precio = models.CharField(
        max_length=10,
        choices=[
            ('bajo', 'Bajo'),
            ('medio', 'Medio'),
            ('alto', 'Alto'),
        ],
    )

    def save(self, *args, **kwargs):
        # Asignar la condición de precio basada en el valor del campo "precio"
        if self.precio <= 10000:
            self.condicion_precio = 'bajo'
        elif self.precio <= 30000:
            self.condicion_precio = 'medio'
        else:
            self.condicion_precio = 'alto'

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.marca} {self.modelo}'
    

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio', 'condicion_precio']

class VisualizarCatalogoPermission(models.Model):
    class Meta:
        permissions = [
            ("visualizar_catalogo", "Puede visualizar Catálogo de Vehículos"),
        ]

    def __str__(self):
        return "Puede visualizar Catálogo de Vehículos"

