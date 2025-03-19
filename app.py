from flask import Flask, render_template

app = Flask(__name__)

@app.route("/galletas")
def galletas():
    return render_template("layout_clientes.html", active_page="galletas")

@app.route("/ventas")
def ventas():
    return render_template("Ventas.html", active_page="ventas")

@app.route("/produccion")
def produccion():
    return render_template("layout_login.html", active_page="produccion")

@app.route("/insumos")
def insumos():
    return render_template("insumos.html", active_page="insumos")

@app.route("/ordenes")
def ordenes():
    return render_template("ordenes.html", active_page="ordenes")

@app.route("/ganancias")
def ganancias():
    return render_template("ganancias.html", active_page="ganancias")

@app.route("/administracion")
def administracion():
    return render_template("Layaut_administracion.html", active_page="administracion")

@app.route("/proveedores")
def proveedores():
    return render_template("Proveedores.html", active_page="proveedores")

@app.route("/usuarios")
def usuarios():
    return render_template("Usuarios.html", active_page="usuarios")

@app.route("/clientes")
def clientes():
    return render_template("Clientes.html", active_page="clientes")

@app.route("/recetas")
def recetas():
    return render_template("Recetas.html", active_page="recetas")


if __name__ == '__main__':
    app.run(debug=True)