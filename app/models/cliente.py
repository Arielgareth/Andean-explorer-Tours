from app.extensions import db


class Cliente(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombres = db.Column(
        db.String(100),
        nullable=False
    )

    apellidos = db.Column(
        db.String(100),
        nullable=False
    )

    telefono = db.Column(
        db.String(20)
    )

    email = db.Column(
        db.String(100)
    )

    pasaporte = db.Column(
        db.String(50)
    )