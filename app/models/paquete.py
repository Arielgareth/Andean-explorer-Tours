
from app.extensions import db


class Paquete(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    destino = db.Column(
        db.String(100),
        nullable=False
    )

    duracion = db.Column(
        db.String(50)
    )

    precio = db.Column(
        db.Float,
        nullable=False
    )

    descripcion = db.Column(
        db.String(300)
    )

