from app.extensions import db


class Vehiculo(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    marca = db.Column(
        db.String(50),
        nullable=False
    )

    modelo = db.Column(
        db.String(50),
        nullable=False
    )

    placa = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    capacidad = db.Column(
        db.Integer,
        nullable=False
    )

    estado = db.Column(
        db.String(30)
    )