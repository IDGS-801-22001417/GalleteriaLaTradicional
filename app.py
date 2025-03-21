<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from flask import flash
from config import DeveplopmentConfig
from sqlalchemy import func, extract
from sqlalchemy.sql import text
import forms
import os
from datetime import datetime
from models import db, Persona, Usuario, Empleado

app = Flask(__name__)
app.config.from_object(DeveplopmentConfig)
csrf = CSRFProtect()
=======
from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf import CSRFProtect
from flask import g
from config import DevelopmentConfig
import forms

from models import db
from models import Insumos, Proveedores, LoteInsumo

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()
>>>>>>> 7e3fd8070f77aff622f8ed40d20694162f7d7252

@app.route("/galletas")
def galletas():
    return render_template("layout_clientes.html", active_page="galletas")

@app.route("/ventas")
def ventas():
<<<<<<< HEAD
    return render_template("Ventas.html", active_page="ventas")
=======
    return render_template("layout_galleteria.html", active_page="ventas")
>>>>>>> 7e3fd8070f77aff622f8ed40d20694162f7d7252

@app.route("/produccion")
def produccion():
    return render_template("layout_login.html", active_page="produccion")

<<<<<<< HEAD
@app.route("/insumos")
def insumos():
    return render_template("insumos.html", active_page="insumos")

@app.route("/ordenes")
=======
@app.route("/insumos", methods=["GET", "POST"])
def insumos():
    create_form=forms.UserForm2(request.form)
    insumos=Insumos.query.all() # select*from insumos
    return render_template("Insumos.html", form=create_form, insumos=insumos, active_page="insumos")

@app.route("/Ordenes")
>>>>>>> 7e3fd8070f77aff622f8ed40d20694162f7d7252
def ordenes():
    return render_template("ordenes.html", active_page="ordenes")

@app.route("/ganancias")
def ganancias():
    return render_template("ganancias.html", active_page="ganancias")

<<<<<<< HEAD
@app.route("/administracion")
def administracion():
    return render_template("Layaut_administracion.html", active_page="administracion")

@app.route("/proveedores")
def proveedores():
    return render_template("Proveedores.html", active_page="proveedores")

@app.route("/usuarios")
def usuarios():
    empleado_class = forms.EmpleadoForm(request.form)
    empleados = Empleado.query.join(Persona).join(Usuario).all()

    return render_template("Usuarios.html", active_page="usuarios", form=empleado_class, empleados=empleados)

@app.route('/registroEmpleado', methods=['GET', 'POST'])
def registroEmpleado():
    empleado_class = forms.EmpleadoForm(request.form)
    empleados = Empleado.query.join(Persona).join(Usuario).all()

    rol_etiquetas = {
        'ADMI': 'Administrador',
        'CAJA': 'Cajero',
        'PROD': 'Producción'
    }

    if request.method == 'POST' and empleado_class.validate():
        try:
            ap_paterno = empleado_class.apPaterno.data[:2].upper()
            ap_materno = empleado_class.apMaterno.data[:2].upper()
            nombre = empleado_class.nombre.data[:2].upper()

            fecha_registro = datetime.now()
            dia_mes = fecha_registro.strftime('%d%m')

            rol = empleado_class.rol.data.upper()

            puesto = rol_etiquetas.get(rol, 'Desconocido')

            nombre_usuario = f"{ap_paterno}{ap_materno}{nombre}{dia_mes}{rol}"

            contrasenia = f"{ap_paterno}{ap_materno}{nombre}{dia_mes}{rol}"
            persona = Persona(
                apPaterno=empleado_class.apPaterno.data,
                apMaterno=empleado_class.apMaterno.data,
                nombre=empleado_class.nombre.data,
                genero=empleado_class.genero.data,
                telefono=empleado_class.telefono.data,
                email=empleado_class.email.data,
                calle=empleado_class.calle.data,
                numero=empleado_class.numero.data,
                colonia=empleado_class.colonia.data,
                codigoPostal=empleado_class.codigoPostal.data,
                fechaNacimiento=empleado_class.fechaNacimiento.data
            )
            db.session.add(persona)
            db.session.commit()
            ultimo_id_persona = persona.idPersona

            usuario = Usuario(
                nombreUsuario=nombre_usuario,
                contrasenia=contrasenia,
                estatus=1,
                rol=empleado_class.rol.data
            )
            db.session.add(usuario)
            db.session.commit()
            ultimo_id_usuario = usuario.idUsuario

            empleado = Empleado(
                puesto=puesto,
                curp=empleado_class.curp.data,
                rfc=empleado_class.rfc.data,
                salarioBruto=empleado_class.salarioBruto.data,
                fechaIngreso=empleado_class.fechaIngreso.data,
                idPersona=ultimo_id_persona,
                idUsuario=ultimo_id_usuario
            )
            db.session.add(empleado)
            db.session.commit()

            flash('Empleado registrado correctamente.', 'success')
            return redirect(url_for('usuarios'))
        except Exception as e:
            db.session.rollback()
            flash('Error al registrar el empleado', 'danger')

    return render_template("Usuarios.html", active_page="usuarios", form=empleado_class, empleados=empleados)

@app.route("/detallesEmpleado", methods=['GET', 'POST'])
def detallesEmpleados():
    if request.method == 'GET':
        idEmpleado = request.args.get('idEmpleado')
        empleado = (
            db.session.query(Empleado)
            .options(db.joinedload(Empleado.persona), db.joinedload(Empleado.usuario))
            .filter(Empleado.idEmpleado == idEmpleado)
            .first()
        )

    return render_template("DetallesEmpleado.html", active_page="usuarios", empleado=empleado)

from flask import request, redirect, url_for, flash

@app.route('/eliminarEmpleado', methods=['GET', 'POST'])
def eliminarEmpleado():
    if request.method == 'GET':
        idEmpleado = request.args.get('idEmpleado') 
        empleado = (
            db.session.query(Empleado)
            .options(db.joinedload(Empleado.persona), db.joinedload(Empleado.usuario))
            .filter(Empleado.idEmpleado == idEmpleado)
            .first()
        )

        if empleado:
            try:
                if empleado.usuario.estatus == 1:
                    empleado.usuario.estatus = 0 
                    db.session.commit() 
                    flash('Empleado desactivado correctamente.', 'success')
                else:
                    flash('El empleado ya está inactivo.', 'warning')
            except Exception as e:
                db.session.rollback()
                flash('Error al desactivar el empleado.', 'danger')
                print(f"Error: {e}")
        else:
            flash('Empleado no encontrado.', 'danger')

        return redirect(url_for('usuarios'))

    return render_template('Usuario.html', active_page="usuarios")

@app.route("/clientes")
def clientes():
    return render_template("Clientes.html", active_page="clientes")

@app.route("/recetas")
def recetas():
    return render_template("Recetas.html", active_page="recetas")

=======
@app.route("/administrador")
def administrador():
    return render_template("administrador.html", active_page="administrador")
>>>>>>> 7e3fd8070f77aff622f8ed40d20694162f7d7252

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
<<<<<<< HEAD
    app.run(debug=True)
=======
app.run()
>>>>>>> 7e3fd8070f77aff622f8ed40d20694162f7d7252
