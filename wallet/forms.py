from django import forms
from .models import Usuario, Cuenta, Transaccion


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre", "apellido", "email", "rut", "activo"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "rut": forms.TextInput(attrs={"class": "form-control", "placeholder": "12345678-9"}),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ["usuario", "numero_cuenta", "tipo", "saldo", "activa"]
        widgets = {
            "usuario": forms.Select(attrs={"class": "form-select"}),
            "numero_cuenta": forms.TextInput(attrs={"class": "form-control"}),
            "tipo": forms.Select(attrs={"class": "form-select"}),
            "saldo": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "activa": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ["cuenta_origen", "cuenta_destino", "tipo", "monto", "descripcion"]
        widgets = {
            "cuenta_origen": forms.Select(attrs={"class": "form-select"}),
            "cuenta_destino": forms.Select(attrs={"class": "form-select"}),
            "tipo": forms.Select(attrs={"class": "form-select"}),
            "monto": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }


class BusquedaTransaccionForm(forms.Form):
    tipo = forms.ChoiceField(
        choices=[("", "Todos")] + Transaccion.TIPOS,
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    monto_min = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "placeholder": "Monto mínimo"}),
    )
    monto_max = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "placeholder": "Monto máximo"}),
    )
    numero_cuenta = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "N° de cuenta"}),
    )
