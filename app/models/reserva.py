from app.extensions import db


class Reserva(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey('cliente.id')
    )

    paquete_id = db.Column(
        db.Integer,
        db.ForeignKey('paquete.id')
    )

    guia_id = db.Column(
        db.Integer,
        db.ForeignKey('guia.id')
    )

    vehiculo_id = db.Column(
        db.Integer,
        db.ForeignKey('vehiculo.id')
    )

    fecha = db.Column(
        db.String(30)
    )

    personas = db.Column(
        db.Integer
    )

    estado = db.Column(
        db.String(30)
    )


    cliente = db.relationship('Cliente')

    paquete = db.relationship('Paquete')

    guia = db.relationship('Guia')

    vehiculo = db.relationship('Vehiculo')