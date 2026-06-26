
from app.extensions import db


class Factura(db.Model):

    __tablename__ = 'factura'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    pago_id = db.Column(
        db.Integer,
        db.ForeignKey('pago.id')
    )

    numero_factura = db.Column(
        db.String(30)
    )

    fecha_emision = db.Column(
        db.String(20)
    )

    nit = db.Column(
        db.String(30)
    )

    razon_social = db.Column(
        db.String(100)
    )

    total = db.Column(
        db.Float
    )

    pago = db.relationship(
        'Pago'
    )