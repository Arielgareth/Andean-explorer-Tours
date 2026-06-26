from datetime import datetime
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required

from app.extensions import db
from app.models.reserva import Reserva
from app.models.cliente import Cliente
from app.models.paquete import Paquete
from app.models.guia import Guia
from app.models.vehiculo import Vehiculo

from app.blueprints.reservas import reservas_bp


def verificar_disponibilidad(fecha_viaje, id_guia, id_vehiculo, pasajeros, reserva_id=None):
    """
    Función de validación lógica para pruebas de caja blanca (PCB-01 a PCB-06).
    Verifica la disponibilidad de guías, vehículos y capacidad física.
    """
    if not isinstance(fecha_viaje, str):
        fecha_viaje = fecha_viaje.strftime('%Y-%m-%d')

    # 1. Validar capacidad del vehículo
    vehiculo = Vehiculo.query.get(id_vehiculo)
    if vehiculo and pasajeros > vehiculo.capacidad:
        return False

    # 2. Validar colisión de agenda del Guía
    query_guia = Reserva.query.filter(
        Reserva.guia_id == id_guia,
        Reserva.fecha == fecha_viaje,
        Reserva.estado != 'Cancelada'
    )
    if reserva_id:
        query_guia = query_guia.filter(Reserva.id != reserva_id)
    if query_guia.first():
        return False

    # 3. Validar colisión de uso del Vehículo
    query_vehiculo = Reserva.query.filter(
        Reserva.vehiculo_id == id_vehiculo,
        Reserva.fecha == fecha_viaje,
        Reserva.estado != 'Cancelada'
    )
    if reserva_id:
        query_vehiculo = query_vehiculo.filter(Reserva.id != reserva_id)
    if query_vehiculo.first():
        return False

    return True


@reservas_bp.route('/reservas')
@login_required
def listar_reservas():
    reservas = Reserva.query.all()
    return render_template(
        'reservas/listar.html',
        reservas=reservas
    )


@reservas_bp.route('/reservas/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_reserva():
    clientes = Cliente.query.all()
    paquetes = Paquete.query.all()
    guias = Guia.query.all()
    vehiculos = Vehiculo.query.all()

    if request.method == 'POST':
        # Extracción alineada a los names de tu formulario HTML de registro
        cliente_id = request.form.get('cliente')
        paquete_id = request.form.get('paquete')
        guia_id = request.form.get('guia')
        vehiculo_id = request.form.get('vehiculo')
        fecha_str = request.form.get('fecha')
        pasajeros = int(request.form.get('personas', 0))
        estado = request.form.get('estado', 'Pendiente')

        id_g = int(guia_id) if guia_id and guia_id.strip() else 0
        id_v = int(vehiculo_id) if vehiculo_id and vehiculo_id.strip() else 0

        if not verificar_disponibilidad(fecha_str, id_g, id_v, pasajeros):
            flash("Error: Conflicto de disponibilidad de recursos o capacidad excedida.", "danger")
            return redirect(url_for('reservas.nuevo_reserva'))

        reserva = Reserva(
            cliente_id=int(cliente_id) if cliente_id else None,
            paquete_id=int(paquete_id) if paquete_id else None,
            guia_id=id_g if id_g else None,
            vehiculo_id=id_v if id_v else None,
            fecha=fecha_str,
            personas=pasajeros,
            estado=estado
        )

        db.session.add(reserva)
        db.session.commit()
        flash("Reserva creada exitosamente.", "success")
        return redirect(url_for('reservas.listar_reservas'))

    return render_template(
        'reservas/nuevo.html',
        clientes=clientes,
        paquetes=paquetes,
        guias=guias,
        vehiculos=vehiculos
    )


@reservas_bp.route('/reservas/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    clientes = Cliente.query.all()
    paquetes = Paquete.query.all()
    guias = Guia.query.all()
    vehiculos = Vehiculo.query.all()

    if request.method == 'POST':
        # Extracción alineada a los names de tu formulario
        cliente_id = request.form.get('cliente')
        paquete_id = request.form.get('paquete')
        guia_id = request.form.get('guia')
        vehiculo_id = request.form.get('vehiculo')
        fecha_str = request.form.get('fecha')
        pasajeros = int(request.form.get('personas', 0))
        estado = request.form.get('estado')

        id_c = int(cliente_id) if cliente_id and cliente_id.strip() else None
        id_p = int(paquete_id) if paquete_id and paquete_id.strip() else None
        id_g = int(guia_id) if guia_id and guia_id.strip() else None
        id_v = int(vehiculo_id) if vehiculo_id and vehiculo_id.strip() else None

        # Validación pasando el ID de la reserva actual para evitar auto-bloqueos
        if not verificar_disponibilidad(fecha_str, id_g or 0, id_v or 0, pasajeros, reserva_id=reserva.id):
            flash("Error: Los recursos seleccionados no están disponibles o superan la capacidad.", "danger")
            return redirect(url_for('reservas.editar_reserva', id=id))

        # Sincronización directa con el modelo de base de datos
        reserva.cliente_id = id_c
        reserva.paquete_id = id_p
        reserva.guia_id = id_g
        reserva.vehiculo_id = id_v
        reserva.fecha = fecha_str
        reserva.personas = pasajeros
        reserva.estado = estado

        db.session.commit()
        flash("Reserva actualizada correctamente.", "success")
        return redirect(url_for('reservas.listar_reservas'))

    return render_template(
        'reservas/editar.html',
        reserva=reserva,
        clientes=clientes,
        paquetes=paquetes,
        guias=guias,
        vehiculos=vehiculos
    )


@reservas_bp.route('/reservas/eliminar/<int:id>')
@login_required
def eliminar_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    db.session.delete(reserva)
    db.session.commit()
    flash("Reserva eliminada del sistema.", "info")
    return redirect(url_for('reservas.listar_reservas'))