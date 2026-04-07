# 💳 Alke Wallet — ABP Módulo 7

Aplicación web para gestión de usuarios y operaciones financieras básicas, desarrollada con **Django + SQLite** como parte del Bootcamp Python con Django.

---

## Tecnologías

- Python 3
- Django 6.0.3
- SQLite
- Bootstrap 5

---

## Modelos de datos

| Modelo | Descripción |
|--------|-------------|
| `Usuario` | Datos personales del cliente (nombre, RUT, email) |
| `Cuenta` | Cuenta bancaria vinculada a un usuario (ahorro/corriente) |
| `Transaccion` | Operación financiera entre cuentas (depósito, retiro, transferencia) |

---

## Funcionalidades

- CRUD completo de Usuarios, Cuentas y Transacciones desde templates propios
- Búsqueda y filtrado de transacciones por tipo, monto y número de cuenta
- Panel de control con estadísticas generales

---

## Instalación y uso

```bash
# 1. Clonar el repositorio
git clone https://github.com/DanielaFMV/abp-alkewallet-modulo7.git
cd abp-alkewallet-modulo7

# 2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# 3. Instalar dependencias
pip install django

# 4. Aplicar migraciones
python manage.py migrate

# 5. Iniciar servidor
python manage.py runserver
```

Abrir en el navegador: **http://127.0.0.1:8000**

---

## Rutas principales

| URL | Descripción |
|-----|-------------|
| `/` | Panel de control |
| `/usuarios/` | Lista de usuarios |
| `/cuentas/` | Lista de cuentas |
| `/transacciones/` | Lista de transacciones |
| `/transacciones/buscar/` | Búsqueda y filtrado |

