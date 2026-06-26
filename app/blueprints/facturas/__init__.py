from flask import Blueprint

facturas_bp = Blueprint(
    'facturas',
    __name__
)

from app.blueprints.facturas import routes