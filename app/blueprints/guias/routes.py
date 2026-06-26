
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from flask_login import current_user
from flask import abort
from app.extensions import db
from app.models.guia import Guia
from app.blueprints.guias import guias_bp


@guias_bp.route('/guias')
@login_required
def listar_guias():

    if current_user.rol != "Administrador":
        abort(403)

    guias = Guia.query.all()

    return render_template(
        'guias/listar.html',
        guias=guias
    )


@guias_bp.route('/guias/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_guia():

    if request.method == 'POST':

        guia = Guia(

            nombre=request.form['nombre'],

            idiomas=request.form['idiomas'],

            certificaciones=request.form['certificaciones']

        )

        db.session.add(guia)

        db.session.commit()

        return redirect(
            url_for('guias.listar_guias')
        )

    return render_template(
        'guias/nuevo.html'
    )


@guias_bp.route('/guias/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_guia(id):

    guia = Guia.query.get_or_404(id)

    if request.method == 'POST':

        guia.nombre = request.form['nombre']

        guia.idiomas = request.form['idiomas']

        guia.certificaciones = request.form['certificaciones']

        db.session.commit()

        return redirect(
            url_for('guias.listar_guias')
        )

    return render_template(
        'guias/editar.html',
        guia=guia
    )


@guias_bp.route('/guias/eliminar/<int:id>')
@login_required
def eliminar_guia(id):

    guia = Guia.query.get_or_404(id)

    db.session.delete(guia)

    db.session.commit()

    return redirect(
        url_for('guias.listar_guias')
    )
