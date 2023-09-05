# Generated by Django 4.0.5 on 2023-09-05 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0005_vehiculo_condicion_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='condicion_precio',
            field=models.CharField(choices=[('bajo', 'Bajo'), ('medio', 'Medio'), ('alto', 'Alto')], max_length=10),
        ),
    ]