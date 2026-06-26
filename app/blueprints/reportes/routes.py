from flask import render_template
from flask_login import login_required

from app.models.usuario import Usuario
from app.models.cliente import Cliente
from app.models.guia import Guia
from app.models.vehiculo import Vehiculo
from app.models.paquete import Paquete
from app.models.reserva import Reserva
from app.models.pago import Pago
from app.models.factura import Factura

from app.blueprints.reportes import reportes_bp

from reportlab.platypus import SimpleDocTemplate, Table

from io import BytesIO
from flask import send_file
import pandas as pd



@reportes_bp.route('/reportes')
@login_required
def reportes():

    total_usuarios = Usuario.query.count()

    total_clientes = Cliente.query.count()

    total_guias = Guia.query.count()

    total_vehiculos = Vehiculo.query.count()

    total_paquetes = Paquete.query.count()

    total_reservas = Reserva.query.count()

    total_pagos = Pago.query.count()

    total_facturas = Factura.query.count()

    return render_template(
        'reportes/index.html',

        total_usuarios=total_usuarios,

        total_clientes=total_clientes,

        total_guias=total_guias,

        total_vehiculos=total_vehiculos,

        total_paquetes=total_paquetes,

        total_reservas=total_reservas,

        total_pagos=total_pagos,

        total_facturas=total_facturas
    )



@reportes_bp.route('/reportes/excel')
@login_required
def reporte_excel():

    archivo = BytesIO()

    # CONSULTAS
    clientes = Cliente.query.all()
    reservas = Reserva.query.all()
    pagos = Pago.query.all()
    facturas = Factura.query.all()

    # CLIENTES
    datos_clientes = []

    for c in clientes:

        datos_clientes.append({

            "ID": c.id,
            "Nombres": c.nombres,
            "Apellidos": c.apellidos,
            "Telefono": c.telefono,
            "Email": c.email,
            "Pasaporte": c.pasaporte

        })

    df_clientes = pd.DataFrame(datos_clientes)


    # RESERVAS
    datos_reservas = []

    for r in reservas:

        datos_reservas.append({

            "ID": r.id,
            "Cliente": r.cliente.nombres,
            "Paquete": r.paquete.nombre,
            "Fecha": r.fecha,
            "Personas": r.personas,
            "Estado": r.estado

        })

    df_reservas = pd.DataFrame(datos_reservas)


    # PAGOS
    datos_pagos = []

    for p in pagos:

        datos_pagos.append({

            "ID": p.id,
            "Reserva": p.reserva.id,
            "Monto": p.monto,
            "Metodo": p.metodo_pago,
            "Fecha": p.fecha_pago

        })

    df_pagos = pd.DataFrame(datos_pagos)


    # FACTURAS
    datos_facturas = []

    for f in facturas:

        datos_facturas.append({

            "ID": f.id,
            "Numero Factura": f.numero_factura,
            "NIT": f.nit,
            "Razon Social": f.razon_social,
            "Total": f.total

        })

    df_facturas = pd.DataFrame(datos_facturas)


    # CREAR EXCEL CON VARIAS HOJAS
    with pd.ExcelWriter(
            archivo,
            engine='openpyxl'
    ) as writer:

        df_clientes.to_excel(
            writer,
            sheet_name='Clientes',
            index=False
        )

        df_reservas.to_excel(
            writer,
            sheet_name='Reservas',
            index=False
        )

        df_pagos.to_excel(
            writer,
            sheet_name='Pagos',
            index=False
        )

        df_facturas.to_excel(
            writer,
            sheet_name='Facturas',
            index=False
        )

    archivo.seek(0)

    return send_file(

        archivo,

        download_name='reporte_general.xlsx',

        as_attachment=True,

        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    )