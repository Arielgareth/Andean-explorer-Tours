from app.extensions import db

class RutaTuristica(db.Model):


    __tablename__ = 'ruta_turistica'

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100))

    origen = db.Column(db.String(100))
    destino = db.Column(db.String(100))

    # ORIGEN
    lat_origen = db.Column(db.Float)
    lon_origen = db.Column(db.Float)

# PUNTO INTERMEDIO
    lat_intermedio = db.Column(db.Float)
    lon_intermedio = db.Column(db.Float)

# DESTINO
    lat_destino = db.Column(db.Float)
    lon_destino = db.Column(db.Float)

    distancia = db.Column(db.Float)

    tiempo = db.Column(db.String(50))

    servicios = db.Column(db.Text)

    descripcion = db.Column(db.Text)

    imagen = db.Column(db.String(200))


