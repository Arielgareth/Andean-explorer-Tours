from flask import render_template, request, redirect, url_for
from flask_login import login_required
from flask_login import current_user
from flask import abort
from app.extensions import db
from app.models.cliente import Cliente
from app.blueprints.clientes import clientes_bp


@clientes_bp.route('/clientes')
@login_required
def listar_clientes():

    if current_user.rol != "Administrador":
        abort(403)

    clientes = Cliente.query.all()

    return render_template(
        'clientes/listar.html',
        clientes=clientes
    )

@clientes_bp.route('/clientes/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_cliente():

    if request.method == 'POST':

        cliente = Cliente(

            nombres=request.form['nombres'],

            apellidos=request.form['apellidos'],

            telefono=request.form['telefono'],

            email=request.form['email'],

            pasaporte=request.form['pasaporte']

        )

        db.session.add(cliente)

        db.session.commit()

        return redirect(
            url_for('clientes.listar_clientes')
        )

    return render_template(
        'clientes/nuevo.html'
    )

@clientes_bp.route('/clientes/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_cliente(id):

    cliente = Cliente.query.get_or_404(id)

    if request.method == 'POST':

        cliente.nombres = request.form['nombres']

        cliente.apellidos = request.form['apellidos']

        cliente.telefono = request.form['telefono']

        cliente.email = request.form['email']

        cliente.pasaporte = request.form['pasaporte']

        db.session.commit()

        return redirect(
            url_for('clientes.listar_clientes')
        )

    return render_template(
        'clientes/editar.html',
        cliente=cliente
    )

@clientes_bp.route('/clientes/eliminar/<int:id>')
@login_required
def eliminar_cliente(id):

    cliente = Cliente.query.get_or_404(id)

    db.session.delete(cliente)

    db.session.commit()

    return redirect(
        url_for('clientes.listar_clientes')
    )