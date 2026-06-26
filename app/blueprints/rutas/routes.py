from flask import render_template, request, redirect, url_for
from flask_login import login_required
from geopy.distance import geodesic

from app.blueprints.rutas import rutas_bp
from app.models.ruta_turistica import RutaTuristica
from app.extensions import db

# ==========================================
# LISTAR RUTAS
# ==========================================
@rutas_bp.route('/rutas')
@login_required
def listar_rutas():
    rutas = RutaTuristica.query.all()
    return render_template('rutas/index.html', rutas=rutas)


# ==========================================
# NUEVA RUTA
# ==========================================
@rutas_bp.route('/rutas/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo():
    if request.method == 'POST':
        # ORIGEN
        lat_origen = float(request.form['lat_origen'])
        lon_origen = float(request.form['lon_origen'])

        # DESTINO
        lat_destino = float(request.form['lat_destino'])
        lon_destino = float(request.form['lon_destino'])

        # INTERMEDIOS (Leemos los nombres 'lat_punto1' del HTML de forma segura)
        p1_lat = request.form.get('lat_punto1')
        p1_lon = request.form.get('lon_punto1')
        
        # Guardamos en variables manejando nulos si vienen vacíos
        lat_intermedio = float(p1_lat) if p1_lat else None
        lon_intermedio = float(p1_lon) if p1_lon else None

        # CÁLCULO DE DISTANCIA INTELIGENTE
        if lat_intermedio and lon_intermedio:
            tramo1 = geodesic((lat_origen, lon_origen), (lat_intermedio, lon_intermedio)).kilometers
            tramo2 = geodesic((lat_intermedio, lon_intermedio), (lat_destino, lon_destino)).kilometers
            distancia = round(tramo1 + tramo2, 2)
        else:
            distancia = round(geodesic((lat_origen, lon_origen), (lat_destino, lon_destino)).kilometers, 2)

        # TIEMPO ESTIMADO (60 km/h)
        horas = distancia / 60
        tiempo = f"{round(horas, 2)} horas"

        nueva_ruta = RutaTuristica(
            nombre=request.form['nombre'],
            origen=request.form['origen'],
            destino=request.form['destino'],
            lat_origen=lat_origen,
            lon_origen=lon_origen,
            lat_intermedio=lat_intermedio, # Cambiado para aceptar None o Float
            lon_intermedio=lon_intermedio,
            lat_destino=lat_destino,
            lon_destino=lon_destino,
            distancia=distancia,
            tiempo=tiempo,
            servicios=request.form['servicios'],
            descripcion=request.form['descripcion'],
            imagen=request.form['imagen']
        )

        db.session.add(nueva_ruta)
        db.session.commit()
        return redirect(url_for('rutas.listar_rutas'))

    return render_template('rutas/nuevo.html')


# ==========================================
# MAPA
# ==========================================
@rutas_bp.route('/rutas/mapa/<int:id>')
@login_required
def mapa(id):
    ruta = RutaTuristica.query.get_or_404(id)
    return render_template('rutas/mapa.html', ruta=ruta)


# ==========================================
# EDITAR
# ==========================================
@rutas_bp.route('/rutas/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    ruta = RutaTuristica.query.get_or_404(id)

    if request.method == 'POST':
        ruta.nombre = request.form['nombre']
        ruta.origen = request.form['origen']
        ruta.destino = request.form['destino']

        ruta.lat_origen = float(request.form['lat_origen'])
        ruta.lon_origen = float(request.form['lon_origen'])
        ruta.lat_destino = float(request.form['lat_destino'])
        ruta.lon_destino = float(request.form['lon_destino'])

        # Capturamos usando 'lat_punto1' para que no explote con tu HTML
        p1_lat = request.form.get('lat_punto1')
        p1_lon = request.form.get('lon_punto1')
        
        ruta.lat_intermedio = float(p1_lat) if p1_lat else None
        ruta.lon_intermedio = float(p1_lon) if p1_lon else None

        # RECALCULAR DISTANCIA EN LA EDICIÓN
        if ruta.lat_intermedio and ruta.lon_intermedio:
            tramo1 = geodesic((ruta.lat_origen, ruta.lon_origen), (ruta.lat_intermedio, ruta.lon_intermedio)).kilometers
            tramo2 = geodesic((ruta.lat_intermedio, ruta.lon_intermedio), (ruta.lat_destino, ruta.lon_destino)).kilometers
            ruta.distancia = round(tramo1 + tramo2, 2)
        else:
            ruta.distancia = round(geodesic((ruta.lat_origen, ruta.lon_origen), (ruta.lat_destino, ruta.lon_destino)).kilometers, 2)

        # RECALCULAR TIEMPO
        horas = ruta.distancia / 60
        ruta.tiempo = f"{round(horas, 2)} horas"

        ruta.servicios = request.form['servicios']
        ruta.descripcion = request.form['descripcion']
        ruta.imagen = request.form['imagen']

        db.session.commit() # Guarda todos los cambios en la DB de forma persistente
        return redirect(url_for('rutas.listar_rutas'))

    return render_template('rutas/editar.html', ruta=ruta)


# ==========================================
# ELIMINAR
# ==========================================
@rutas_bp.route('/rutas/eliminar/<int:id>')
@login_required
def eliminar(id):
    ruta = RutaTuristica.query.get_or_404(id)
    db.session.delete(ruta)
    db.session.commit()
    return redirect(url_for('rutas.listar_rutas'))