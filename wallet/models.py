from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    rut = models.CharField(max_length=12, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name_plural = "Usuarios"
        ordering = ["apellido", "nombre"]


class Cuenta(models.Model):
    TIPOS = [
        ("ahorro", "Ahorro"),
        ("corriente", "Corriente"),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="cuentas")
    numero_cuenta = models.CharField(max_length=20, unique=True)
    tipo = models.CharField(max_length=10, choices=TIPOS, default="ahorro")
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.numero_cuenta} ({self.get_tipo_display()}) — {self.usuario}"

    class Meta:
        verbose_name_plural = "Cuentas"
        ordering = ["-fecha_creacion"]


class Transaccion(models.Model):
    TIPOS = [
        ("deposito", "Depósito"),
        ("retiro", "Retiro"),
        ("transferencia", "Transferencia"),
    ]

    cuenta_origen = models.ForeignKey(
        Cuenta, on_delete=models.PROTECT, related_name="transacciones_origen"
    )
    cuenta_destino = models.ForeignKey(
        Cuenta,
        on_delete=models.PROTECT,
        related_name="transacciones_destino",
        null=True,
        blank=True,
    )
    tipo = models.CharField(max_length=15, choices=TIPOS)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_tipo_display()} — ${self.monto} ({self.fecha.strftime('%d/%m/%Y')})"

    class Meta:
        verbose_name_plural = "Transacciones"
        ordering = ["-fecha"]
