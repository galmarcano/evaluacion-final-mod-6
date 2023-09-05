# Generated by Django 4.0.5 on 2023-09-05 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0003_alter_vehiculo_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisualizarCatalogoPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': [('visualizar_catalogo', 'Puede visualizar Catálogo de Vehículos')],
            },
        ),
    ]