from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario, Cuenta, Transaccion
from .forms import UsuarioForm, CuentaForm, TransaccionForm, BusquedaTransaccionForm


def inicio(request):
    total_usuarios = Usuario.objects.count()
    total_cuentas = Cuenta.objects.count()
    total_transacciones = Transaccion.objects.count()
    ultimas_transacciones = Transaccion.objects.select_related("cuenta_origen__usuario")[:5]
    return render(request, "wallet/inicio.html", {
        "total_usuarios": total_usuarios,
        "total_cuentas": total_cuentas,
        "total_transacciones": total_transacciones,
        "ultimas_transacciones": ultimas_transacciones,
    })


# --- USUARIOS ---

def usuario_lista(request):
    usuarios = Usuario.objects.all()
    return render(request, "wallet/usuarios/lista.html", {"usuarios": usuarios})


def usuario_detalle(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, "wallet/usuarios/detalle.html", {"usuario": usuario})


def usuario_crear(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuario_lista")
    else:
        form = UsuarioForm()
    return render(request, "wallet/usuarios/formulario.html", {"form": form, "titulo": "Nuevo Usuario"})


def usuario_editar(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect("usuario_detalle", pk=usuario.pk)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, "wallet/usuarios/formulario.html", {"form": form, "titulo": "Editar Usuario"})


def usuario_eliminar(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        usuario.delete()
        return redirect("usuario_lista")
    return render(request, "wallet/usuarios/confirmar_eliminar.html", {"usuario": usuario})


# --- CUENTAS ---

def cuenta_lista(request):
    cuentas = Cuenta.objects.select_related("usuario").all()
    return render(request, "wallet/cuentas/lista.html", {"cuentas": cuentas})


def cuenta_detalle(request, pk):
    cuenta = get_object_or_404(Cuenta, pk=pk)
    transacciones = cuenta.transacciones_origen.all()[:10]
    return render(request, "wallet/cuentas/detalle.html", {"cuenta": cuenta, "transacciones": transacciones})


def cuenta_crear(request):
    if request.method == "POST":
        form = CuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cuenta_lista")
    else:
        form = CuentaForm()
    return render(request, "wallet/cuentas/formulario.html", {"form": form, "titulo": "Nueva Cuenta"})


def cuenta_editar(request, pk):
    cuenta = get_object_or_404(Cuenta, pk=pk)
    if request.method == "POST":
        form = CuentaForm(request.POST, instance=cuenta)
        if form.is_valid():
            form.save()
            return redirect("cuenta_detalle", pk=cuenta.pk)
    else:
        form = CuentaForm(instance=cuenta)
    return render(request, "wallet/cuentas/formulario.html", {"form": form, "titulo": "Editar Cuenta"})


def cuenta_eliminar(request, pk):
    cuenta = get_object_or_404(Cuenta, pk=pk)
    if request.method == "POST":
        cuenta.delete()
        return redirect("cuenta_lista")
    return render(request, "wallet/cuentas/confirmar_eliminar.html", {"cuenta": cuenta})


# --- TRANSACCIONES ---

def transaccion_lista(request):
    transacciones = Transaccion.objects.select_related("cuenta_origen__usuario", "cuenta_destino__usuario").all()
    return render(request, "wallet/transacciones/lista.html", {"transacciones": transacciones})


def transaccion_crear(request):
    if request.method == "POST":
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("transaccion_lista")
    else:
        form = TransaccionForm()
    return render(request, "wallet/transacciones/formulario.html", {"form": form, "titulo": "Nueva Transacción"})


def transaccion_eliminar(request, pk):
    transaccion = get_object_or_404(Transaccion, pk=pk)
    if request.method == "POST":
        transaccion.delete()
        return redirect("transaccion_lista")
    return render(request, "wallet/transacciones/confirmar_eliminar.html", {"transaccion": transaccion})


def transaccion_buscar(request):
    form = BusquedaTransaccionForm(request.GET or None)
    transacciones = Transaccion.objects.select_related("cuenta_origen__usuario", "cuenta_destino__usuario").all()

    if form.is_valid():
        tipo = form.cleaned_data.get("tipo")
        monto_min = form.cleaned_data.get("monto_min")
        monto_max = form.cleaned_data.get("monto_max")
        numero_cuenta = form.cleaned_data.get("numero_cuenta")

        if tipo:
            transacciones = transacciones.filter(tipo=tipo)
        if monto_min is not None:
            transacciones = transacciones.filter(monto__gte=monto_min)
        if monto_max is not None:
            transacciones = transacciones.filter(monto__lte=monto_max)
        if numero_cuenta:
            transacciones = transacciones.filter(cuenta_origen__numero_cuenta__icontains=numero_cuenta)

    return render(request, "wallet/transacciones/buscar.html", {"form": form, "transacciones": transacciones})
