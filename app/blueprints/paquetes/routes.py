
from flask import render_template, request, redirect, url_for
from flask_login import login_required

from app.extensions import db
from app.models.paquete import Paquete
from app.blueprints.paquetes import paquetes_bp


@paquetes_bp.route('/paquetes')
@login_required
def listar_paquetes():

    paquetes = Paquete.query.all()

    return render_template(
        'paquetes/listar.html',
        paquetes=paquetes
    )


@paquetes_bp.route('/paquetes/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_paquete():

    if request.method == 'POST':

        paquete = Paquete(

            nombre=request.form['nombre'],

            destino=request.form['destino'],

            duracion=request.form['duracion'],

            precio=request.form['precio'],

            descripcion=request.form['descripcion']

        )

        db.session.add(paquete)

        db.session.commit()

        return redirect(
            url_for('paquetes.listar_paquetes')
        )

    return render_template(
        'paquetes/nuevo.html'
    )


@paquetes_bp.route('/paquetes/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_paquete(id):

    paquete = Paquete.query.get_or_404(id)

    if request.method == 'POST':

        paquete.nombre = request.form['nombre']

        paquete.destino = request.form['destino']

        paquete.duracion = request.form['duracion']

        paquete.precio = request.form['precio']

        paquete.descripcion = request.form['descripcion']

        db.session.commit()

        return redirect(
            url_for('paquetes.listar_paquetes')
        )

    return render_template(
        'paquetes/editar.html',
        paquete=paquete
    )


@paquetes_bp.route('/paquetes/eliminar/<int:id>')
@login_required
def eliminar_paquete(id):

    paquete = Paquete.query.get_or_404(id)

    db.session.delete(paquete)

    db.session.commit()

    return redirect(
        url_for('paquetes.listar_paquetes')
    )

