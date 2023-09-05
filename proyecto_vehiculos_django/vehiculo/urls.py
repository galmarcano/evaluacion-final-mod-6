from django.urls import path
from .views import v_index
from .views import ingresar_vehiculo, listar_vehiculos
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', v_index, name='index'),
    path('add/', ingresar_vehiculo, name='ingresar_vehiculo'),
    path('listar/', listar_vehiculos, name='listar_vehiculos'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]