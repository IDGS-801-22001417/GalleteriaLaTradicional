from flask import Flask, render_template

app = Flask(__name__)

@app.route("/galletas")
def galletas():
    return render_template("layout_clientes.html", active_page="galletas")

@app.route("/ventas")
def ventas():
    return render_template("layout_galleteria.html", active_page="ventas")

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

@app.route("/administrador")
def administrador():
    return render_template("administrador.html", active_page="administrador")

if __name__ == '__main__':
    app.run(debug=True)
    
if __name__ == "__main__":
    app.run(debug=True, port=3000)