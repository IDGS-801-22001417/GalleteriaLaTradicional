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

@app.route("/galletas")
def galletas():
    return render_template("layout_clientes.html", active_page="galletas")

@app.route("/ventas")
def ventas():
    return render_template("layout_galleteria.html", active_page="ventas")

@app.route("/produccion")
def produccion():
    return render_template("layout_login.html", active_page="produccion")

@app.route("/insumos", methods=["GET", "POST"])
def insumos():
    create_form=forms.UserForm2(request.form)
    insumos=Insumos.query.all() # select*from insumos
    return render_template("Insumos.html", form=create_form, insumos=insumos, active_page="insumos")

@app.route("/Ordenes")
def ordenes():
    return render_template("ordenes.html", active_page="ordenes")

@app.route("/ganancias")
def ganancias():
    return render_template("ganancias.html", active_page="ganancias")

@app.route("/administrador")
def administrador():
    return render_template("administrador.html", active_page="administrador")

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
app.run()