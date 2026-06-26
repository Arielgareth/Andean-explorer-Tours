from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from app.extensions import db, login_manager
from app.models.usuario import Usuario
from app.blueprints.auth import auth_bp
from app.blueprints.usuarios import usuarios_bp
from app.blueprints.clientes import clientes_bp
from app.blueprints.guias import guias_bp
from app.blueprints.vehiculos import vehiculos_bp
from app.blueprints.paquetes import paquetes_bp
from app.blueprints.reservas import reservas_bp
from app.blueprints.pagos import pagos_bp
from app.blueprints.facturas import facturas_bp
from app.blueprints.reportes import reportes_bp
from app.blueprints.rutas import rutas_bp


from app.models.usuario import Usuario
from app.models.cliente import Cliente
from app.models.guia import Guia    
from app.models.vehiculo import Vehiculo
from app.models.paquete import Paquete
from app.models.reserva import Reserva
from app.models.pago import Pago
from app.models.factura import Factura
from flask_login import login_required
from app.models.ruta_turistica import RutaTuristica



def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    login_manager.init_app(app)

    app.register_blueprint(auth_bp)

    app.register_blueprint(usuarios_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(guias_bp)
    app.register_blueprint(vehiculos_bp)
    app.register_blueprint(paquetes_bp)
    app.register_blueprint(reservas_bp)
    app.register_blueprint(facturas_bp)
    app.register_blueprint(pagos_bp)
    app.register_blueprint(reportes_bp)
    app.register_blueprint(rutas_bp)
    @app.route('/')
    def inicio():
        return redirect(url_for('auth.login'))
    
    @app.route('/dashboard')
    def dashboard():

        return render_template(
            'dashboard.html',

            total_usuarios=Usuario.query.count(),
            
            total_clientes=Cliente.query.count(),

            total_guias=Guia.query.count(),

            total_vehiculos=Vehiculo.query.count(),

            total_paquetes=Paquete.query.count(),

            total_reservas=Reserva.query.count(),

            total_pagos=Pago.query.count(),

            total_facturas=Factura.query.count()
        )


    @login_manager.user_loader
    def load_user(id):

        return Usuario.query.get(
            int(id)
        )

    return app