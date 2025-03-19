from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Proveedores(db.Model):
    __tablename__ = 'proveedores'
    id_proveedor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    empresa = db.Column(db.String(100), nullable=False)
    fechaRegistro = db.Column(db.Date, nullable=False)
    estatus = db.Column(db.Integer, nullable=False, default=1)  # 0: Inactivo; 1: Fijo; 2: Temporal

    # Relación con la tabla Insumos
    insumos = db.relationship('Insumos', backref='proveedor', lazy=True)

class Insumos(db.Model):
    __tablename__ = 'insumos'
    id_insumo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreInsumo = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(30), nullable=False)
    unidad = db.Column(db.String(50), nullable=False)
    total = db.Column(db.Float, nullable=False)
    id_proveedor = db.Column(db.Integer, db.ForeignKey('proveedores.id_proveedor'), nullable=False)

    # Relación con la tabla LoteInsumo
    lotes = db.relationship('LoteInsumo', backref='insumo', lazy=True)

class LoteInsumo(db.Model):
    __tablename__ = 'loteinsumo'
    idLote = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_insumo = db.Column(db.Integer, db.ForeignKey('insumos.id_insumo'), nullable=False)
    fechaIngreso = db.Column(db.Date, nullable=False)
    fechaCaducidad = db.Column(db.Date, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    costo = db.Column(db.Numeric(10, 2), nullable=False)