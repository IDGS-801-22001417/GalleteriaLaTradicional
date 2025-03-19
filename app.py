from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", active_page="home")

@app.route("/galletas")
def galletas():
    return render_template("galletas.html", active_page="galletas")

@app.route("/ventas")
def ventas():
    return render_template("layout_galleteria.html", active_page="ventas")

@app.route("/produccion")
def produccion():
    galletas = [
        {"id": 1, "nombre": "Chocolate", "ingredientes": ["4 kg de harina de trigo", "2.5 kg de mantequilla", "2.5 kg de azúcar", "1.5 kg de chispas de chocolate", "1 litro de leche", "50 g de sal", "50 g de cacao"]},
        {"id": 2, "nombre": "Arándano", "ingredientes": ["5 kg de harina de trigo", "2.5 kg de mantequilla", "2.5 kg de azúcar", "1.5 kg de arándanos secos", "1 litro de leche", "50 g de sal"]},
        {"id": 3, "nombre": "Avena", "ingredientes": ["3 kg de avena", "2.5 kg de harina", "2.5 kg de azúcar", "1 litro de leche", "50 g de sal", "1 kg de pasas"]},
        {"id": 4, "nombre": "Vainilla", "ingredientes": ["5 kg de harina", "2.5 kg de mantequilla", "2.5 kg de azúcar", "50 g de esencia de vainilla", "1 litro de leche", "50 g de sal"]},
        {"id": 5, "nombre": "Chispas de Chocolate", "ingredientes": ["5 kg de harina", "2.5 kg de mantequilla", "2.5 kg de azúcar", "2 kg de chispas de chocolate", "1 litro de leche", "50 g de sal"]},
        {"id": 6, "nombre": "Limón", "ingredientes": ["5 kg de harina", "2.5 kg de mantequilla", "2.5 kg de azúcar", "200 ml de jugo de limón", "Ralladura de 20 limones"]},
        {"id": 7, "nombre": "Almendra", "ingredientes": ["5 kg de harina", "2.5 kg de mantequilla", "2.5 kg de azúcar", "1.5 kg de almendras troceadas", "1 litro de leche"]},
        {"id": 8, "nombre": "Coco", "ingredientes": ["4 kg de harina", "2.5 kg de mantequilla", "2.5 kg de azúcar", "2 kg de coco rallado", "1 litro de leche"]},
        {"id": 9, "nombre": "Jengibre", "ingredientes": ["4 kg de harina", "2.5 kg de mantequilla", "2.5 kg de azúcar", "500 g de miel", "200 g de jengibre en polvo", "50 g de canela en polvo"]},
        {"id": 10, "nombre": "Sorpresa Nuez", "ingredientes": ["5 kg de harina", "2.5 kg de mantequilla", "2.5 kg de azúcar", "1.5 kg de nueces troceadas", "1 litro de leche"]}
    ]
    return render_template("produccion.html", active_page="produccion", galletas=galletas)


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

if __name__ == "__main__":
    app.run(debug=True, port=3000)
