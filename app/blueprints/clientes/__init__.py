from flask import Blueprint

clientes_bp = Blueprint(
    'clientes',
    __name__
)

from app.blueprints.clientes.routes import *