
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from flask_login import current_user
from flask import abort
from app.extensions import db
from app.models.usuario import Usuario
from app.blueprints.usuarios import usuarios_bp


# LISTAR USUARIOS
@usuarios_bp.route('/usuarios')
@login_required
def listar_usuarios():

    if current_user.rol != "Administrador":
        
        abort(403)

    usuarios = Usuario.query.all()

    return render_template(
        'usuarios/listar.html',
        usuarios=usuarios
    )


# CREAR USUARIO
@usuarios_bp.route('/usuarios/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_usuario():

    if request.method == 'POST':

        usuario = Usuario(

            nombre=request.form['nombre'],

            email=request.form['email'],

            password=request.form['password'],

            rol=request.form['rol']

        )

        db.session.add(usuario)

        db.session.commit()

        return redirect(
            url_for('usuarios.listar_usuarios')
        )

    return render_template(
        'usuarios/nuevo.html'
    )


# EDITAR USUARIO
@usuarios_bp.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_usuario(id):

    usuario = Usuario.query.get_or_404(id)

    if request.method == 'POST':

        usuario.nombre = request.form['nombre']

        usuario.email = request.form['email']

        usuario.rol = request.form['rol']

        db.session.commit()

        return redirect(
            url_for('usuarios.listar_usuarios')
        )

    return render_template(
        'usuarios/editar.html',
        usuario=usuario
    )


# ELIMINAR USUARIO
@usuarios_bp.route('/usuarios/eliminar/<int:id>')
@login_required
def eliminar_usuario(id):

    usuario = Usuario.query.get_or_404(id)

    db.session.delete(usuario)

    db.session.commit()

    return redirect(
        url_for('usuarios.listar_usuarios')
    )
