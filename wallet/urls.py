from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),

    path("usuarios/", views.usuario_lista, name="usuario_lista"),
    path("usuarios/nuevo/", views.usuario_crear, name="usuario_crear"),
    path("usuarios/<int:pk>/", views.usuario_detalle, name="usuario_detalle"),
    path("usuarios/<int:pk>/editar/", views.usuario_editar, name="usuario_editar"),
    path("usuarios/<int:pk>/eliminar/", views.usuario_eliminar, name="usuario_eliminar"),

    path("cuentas/", views.cuenta_lista, name="cuenta_lista"),
    path("cuentas/nueva/", views.cuenta_crear, name="cuenta_crear"),
    path("cuentas/<int:pk>/", views.cuenta_detalle, name="cuenta_detalle"),
    path("cuentas/<int:pk>/editar/", views.cuenta_editar, name="cuenta_editar"),
    path("cuentas/<int:pk>/eliminar/", views.cuenta_eliminar, name="cuenta_eliminar"),

    path("transacciones/", views.transaccion_lista, name="transaccion_lista"),
    path("transacciones/nueva/", views.transaccion_crear, name="transaccion_crear"),
    path("transacciones/<int:pk>/eliminar/", views.transaccion_eliminar, name="transaccion_eliminar"),
    path("transacciones/buscar/", views.transaccion_buscar, name="transaccion_buscar"),
]
