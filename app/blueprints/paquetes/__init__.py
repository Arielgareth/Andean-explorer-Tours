
from flask import Blueprint

paquetes_bp = Blueprint(
    'paquetes',
    __name__
)

from app.blueprints.paquetes.routes import *
