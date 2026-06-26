from app.extensions import db


class Pago(db.Model):

    __tablename__ = 'pago'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    reserva_id = db.Column(
        db.Integer,
        db.ForeignKey('reserva.id')
    )

    fecha_pago = db.Column(
        db.String(20)
    )

    monto = db.Column(
        db.Float
    )

    metodo_pago = db.Column(
        db.String(50)
    )

    estado = db.Column(
        db.String(30)
    )

    reserva = db.relationship(
        'Reserva'
    )