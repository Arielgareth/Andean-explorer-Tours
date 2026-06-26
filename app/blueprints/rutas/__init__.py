from flask import Blueprint

rutas_bp = Blueprint(
    'rutas',
    __name__
)
from app.blueprints.rutas import routes