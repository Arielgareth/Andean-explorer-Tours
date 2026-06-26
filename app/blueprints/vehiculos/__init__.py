from flask import Blueprint

vehiculos_bp = Blueprint(
    'vehiculos',
    __name__
)

from app.blueprints.vehiculos.routes import *