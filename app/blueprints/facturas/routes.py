from flask import render_template, request, redirect, url_for
from flask_login import login_required
from flask_login import current_user
from flask import abort
from app.extensions import db
from app.models.factura import Factura
from app.models.pago import Pago

from app.blueprints.facturas import facturas_bp


@facturas_bp.route('/facturas')
@login_required
def listar_facturas():
    if current_user.rol != "Administrador":
        abort(403)

    facturas = Factura.query.all()

    return render_template(
        'facturas/listar.html',
        facturas=facturas
    )


@facturas_bp.route('/facturas/nuevo',
                    methods=['GET', 'POST'])
@login_required
def nuevo_factura():

    if request.method == 'POST':

        factura = Factura(

            pago_id=request.form['pago'],

            numero_factura=request.form['numero_factura'],

            fecha_emision=request.form['fecha_emision'],

            nit=request.form['nit'],

            razon_social=request.form['razon_social'],

            total=request.form['total']

        )

        db.session.add(
            factura
        )

        db.session.commit()

        return redirect(
            url_for('facturas.listar_facturas')
        )

    pagos = Pago.query.all()

    return render_template(
        'facturas/nuevo.html',
        pagos=pagos
    )


@facturas_bp.route('/facturas/editar/<int:id>',
                    methods=['GET', 'POST'])
@login_required
def editar_factura(id):

    factura = Factura.query.get_or_404(id)

    if request.method == 'POST':

        factura.numero_factura = request.form['numero_factura']

        factura.fecha_emision = request.form['fecha_emision']

        factura.nit = request.form['nit']

        factura.razon_social = request.form['razon_social']

        factura.total = request.form['total']

        db.session.commit()

        return redirect(
            url_for('facturas.listar_facturas')
        )

    return render_template(
        'facturas/editar.html',
        factura=factura
    )


@facturas_bp.route('/facturas/eliminar/<int:id>')
@login_required
def eliminar_factura(id):

    factura = Factura.query.get_or_404(id)

    db.session.delete(
        factura
    )

    db.session.commit()

    return redirect(
        url_for('facturas.listar_facturas')
    )