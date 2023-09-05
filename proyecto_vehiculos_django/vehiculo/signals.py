from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

@receiver(post_save, sender=User)
def asignar_permiso_visualizar_catalogo(sender, instance, created, **kwargs):
    if created:
        # Asignar el permiso "visualizar_catalogo" al usuario
        permission = Permission.objects.get(codename='visualizar_catalogo')
        instance.user_permissions.add(permission)

        # Opcionalmente, agregar el usuario a un grupo (por ejemplo, "Usuarios")
        group, created = Group.objects.get_or_create(name='Usuarios')
        instance.groups.add(group)
