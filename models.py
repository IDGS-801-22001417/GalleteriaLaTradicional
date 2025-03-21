from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

class Persona(db.Model):
    __tablename__ = 'persona'
    idPersona = db.Column(db.Integer, primary_key=True, autoincrement=True)
    apPaterno = db.Column(db.String(20), nullable=False)
    apMaterno = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    genero = db.Column(db.String(1), nullable=False, default="O") 
    telefono = db.Column(db.String(10), nullable=False)
    calle = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    colonia = db.Column(db.String(50), nullable=False)
    codigoPostal = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    fechaNacimiento = db.Column(db.Date, nullable=False)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreUsuario = db.Column(db.String(20), unique=True, nullable=False)
    token = db.Column(db.String(255))
    estatus = db.Column(db.Integer, nullable=False, default=1)
    contrasenia = db.Column(db.String(16), nullable=False)
    rol = db.Column(db.String(4), nullable=False)
    ultima_conexion = db.Column(db.DateTime)

class Empleado(db.Model):
    __tablename__ = 'empleado'
    idEmpleado = db.Column(db.Integer, primary_key=True, autoincrement=True)
    puesto = db.Column(db.String(45), nullable=False)
    curp = db.Column(db.String(18), nullable=False)
    rfc = db.Column(db.String(13), nullable=False)
    salarioBruto = db.Column(db.Float, nullable=False)
    fechaIngreso = db.Column(db.Date, nullable=False)
    idPersona = db.Column(db.Integer, db.ForeignKey('persona.idPersona'), nullable=False)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'), nullable=False)

    persona = db.relationship('Persona', backref=db.backref('empleados', cascade='all, delete-orphan'))
    usuario = db.relationship('Usuario', backref=db.backref('empleados', cascade='all, delete-orphan'))