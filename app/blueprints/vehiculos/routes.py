from flask import render_template, request, redirect, url_for
from flask_login import login_required
from flask_login import current_user
from flask import abort

from app.extensions import db
from app.models.vehiculo import Vehiculo
from app.blueprints.vehiculos import vehiculos_bp


@vehiculos_bp.route('/vehiculos')
@login_required
def listar_vehiculos():

    if current_user.rol != "Administrador":
        abort(403)

    vehiculos = Vehiculo.query.all()

    return render_template(
        'vehiculos/listar.html',
        vehiculos=vehiculos
    )


@vehiculos_bp.route('/vehiculos/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_vehiculo():

    if request.method == 'POST':

        vehiculo = Vehiculo(

            marca=request.form['marca'],

            modelo=request.form['modelo'],

            placa=request.form['placa'],

            capacidad=request.form['capacidad'],

            estado=request.form['estado']

        )

        db.session.add(vehiculo)

        db.session.commit()

        return redirect(
            url_for('vehiculos.listar_vehiculos')
        )

    return render_template(
        'vehiculos/nuevo.html'
    )


@vehiculos_bp.route('/vehiculos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_vehiculo(id):

    vehiculo = Vehiculo.query.get_or_404(id)

    if request.method == 'POST':

        vehiculo.marca = request.form['marca']

        vehiculo.modelo = request.form['modelo']

        vehiculo.placa = request.form['placa']

        vehiculo.capacidad = request.form['capacidad']

        vehiculo.estado = request.form['estado']

        db.session.commit()

        return redirect(
            url_for('vehiculos.listar_vehiculos')
        )

    return render_template(
        'vehiculos/editar.html',
        vehiculo=vehiculo
    )


@vehiculos_bp.route('/vehiculos/eliminar/<int:id>')
@login_required
def eliminar_vehiculo(id):

    vehiculo = Vehiculo.query.get_or_404(id)

    db.session.delete(vehiculo)

    db.session.commit()

    return redirect(
        url_for('vehiculos.listar_vehiculos')
    )