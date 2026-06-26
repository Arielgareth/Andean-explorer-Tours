from flask import Blueprint

reservas_bp = Blueprint(
    'reservas',
    __name__
)

from app.blueprints.reservas.routes import *