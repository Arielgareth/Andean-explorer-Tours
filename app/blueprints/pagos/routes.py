from flask import render_template, request, redirect, url_for
from flask_login import login_required

from app.extensions import db
from app.models.pago import Pago
from app.models.reserva import Reserva

from app.blueprints.pagos import pagos_bp


@pagos_bp.route('/pagos')
@login_required
def listar_pagos():

    pagos = Pago.query.all()

    return render_template(
        'pagos/listar.html',
        pagos=pagos
    )


@pagos_bp.route('/pagos/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_pago():

    if request.method == 'POST':

        pago = Pago(

            reserva_id=request.form['reserva'],

            fecha_pago=request.form['fecha_pago'],

            monto=request.form['monto'],

            metodo_pago=request.form['metodo_pago'],

            estado=request.form['estado']

        )

        db.session.add(
            pago
        )

        db.session.commit()

        return redirect(
            url_for('pagos.listar_pagos')
        )

    reservas = Reserva.query.all()

    return render_template(
        'pagos/nuevo.html',
        reservas=reservas
    )


@pagos_bp.route('/pagos/editar/<int:id>',
                methods=['GET', 'POST'])
@login_required
def editar_pago(id):

    pago = Pago.query.get_or_404(id)

    if request.method == 'POST':

        pago.fecha_pago = request.form['fecha_pago']

        pago.monto = request.form['monto']

        pago.metodo_pago = request.form['metodo_pago']

        pago.estado = request.form['estado']

        db.session.commit()

        return redirect(
            url_for('pagos.listar_pagos')
        )

    return render_template(
        'pagos/editar.html',
        pago=pago
    )


@pagos_bp.route('/pagos/eliminar/<int:id>')
@login_required
def eliminar_pago(id):

    pago = Pago.query.get_or_404(id)

    db.session.delete(
        pago
    )

    db.session.commit()

    return redirect(
        url_for('pagos.listar_pagos')
    )