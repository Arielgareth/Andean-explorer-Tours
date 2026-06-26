from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.extensions import db
from app.models.usuario import Usuario
from app.blueprints.auth import auth_bp


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        usuario = Usuario.query.filter_by(
            email=email
        ).first()

        if usuario and usuario.password == password:

            login_user(usuario)

            return redirect(
                url_for('dashboard')
            )

        flash("Credenciales incorrectas")

    return render_template(
        'login.html'
    )


@auth_bp.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect(
        url_for('auth.login')
    )

@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():

    if request.method == 'POST':

        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']

        existe = Usuario.query.filter_by(
            email=email
        ).first()

        if existe:

            flash("El correo ya está registrado")

            return redirect(
                url_for('auth.registro')
            )

        nuevo_usuario = Usuario(

            nombre=nombre,

            email=email,

            password=password,

            rol='Usuario'
        )

        db.session.add(
            nuevo_usuario
        )

        db.session.commit()

        flash("Usuario creado correctamente")

        return redirect(
            url_for('auth.login')
        )

    return render_template(
        'registro.html'
    )