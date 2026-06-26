
from app.extensions import db


class Guia(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    idiomas = db.Column(
        db.String(100)
    )

    certificaciones = db.Column(
        db.String(100)
    )

