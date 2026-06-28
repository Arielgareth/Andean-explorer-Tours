# Andean Explorer Tours

## Descripción

Andean Explorer Tours es una aplicación web desarrollada en **Python** utilizando **Flask** bajo el patrón **Application Factory**. El sistema permite administrar una agencia de turismo mediante la gestión de usuarios, clientes, paquetes turísticos, reservas, guías, vehículos, rutas, pagos y facturación.

Este proyecto fue desarrollado como Proyecto Final del Curso I-2026.

---

## Tecnologías utilizadas

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- Jinja2

---

## Funcionalidades

- Inicio de sesión de usuarios
- Administración de usuarios
- Gestión de clientes
- Gestión de paquetes turísticos
- Gestión de rutas
- Gestión de guías
- Gestión de vehículos
- Gestión de reservas
- Gestión de pagos
- Gestión de facturas
- Dashboard con estadísticas

---

## Base de datos

El sistema utiliza una base de datos relacional SQLite con tablas relacionadas mediante claves primarias y foráneas.

---

## Instalación

Clonar el repositorio

```bash
git clone https://github.com/Arielgareth/Andean-explorer-Tours.git
```

Entrar al proyecto

```bash
cd Andean-explorer-Tours
```

Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno virtual

Windows

```bash
venv\Scripts\activate
```

Linux o macOS

```bash
source venv/bin/activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación

```bash
python run.py
```

---

## Estructura del proyecto

```
app/
├── auth/
├── dashboard/
├── clientes/
├── usuarios/
├── paquetes/
├── reservas/
├── rutas/
├── guias/
├── vehiculos/
├── pagos/
├── facturas/
├── models/
├── templates/
├── static/
```

---

## Despliegue

Aplicación Web:

https://andean-explorer-tours.onrender.com

---

## Repositorio

https://github.com/Arielgareth/Andean-explorer-Tours

---

## Autor

Proyecto desarrollado para la asignatura de Desarrollo Web con Python y Flask.

Universidad — Gestión I/2026.
