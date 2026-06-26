from flask import Blueprint

pagos_bp = Blueprint(
    'pagos',
    __name__
)

from app.blueprints.pagos import routes