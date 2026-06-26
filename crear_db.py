import os
from app import create_app
from app.extensions import db

# MODELOS
from app.models.usuario import Usuario
from app.models.cliente import Cliente
from app.models.guia import Guia
from app.models.vehiculo import Vehiculo
from app.models.paquete import Paquete
from app.models.reserva import Reserva
from app.models.pago import Pago
from app.models.factura import Factura
from app.models.ruta_turistica import RutaTuristica

app = create_app()

with app.app_context():

    db.create_all()

    print("Base de datos creada correctamente")

