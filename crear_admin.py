from app import create_app
from app.extensions import db
from app.models.usuario import Usuario

app = create_app()

with app.app_context():

    db.create_all()

    admin = Usuario(

        nombre='Administrador',

        email='admin@gmail.com',

        password='123456',

        rol='Administrador'
    )

    db.session.add(admin)

    db.session.commit()

    print(
        "Administrador creado"
    )