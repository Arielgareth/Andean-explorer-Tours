
from flask import Blueprint

guias_bp = Blueprint(
    'guias',
    __name__
)

from app.blueprints.guias.routes import *

