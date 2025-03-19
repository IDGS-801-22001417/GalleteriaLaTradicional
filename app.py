from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf import CSRFProtect
from flask import g
from config import DevelopmentConfig
from models import db
from models import Receta
import forms
import json
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect() 



@app.route('/')
def index():
    
    return render_template('layout_galleteria.html')

@app.route('/recetas', methods=['GET', 'POST'])
def recetas():
    receta_form = forms.RecetaForm(request.form)
    
    if request.method == 'POST' and receta_form.validate():
        nombre = receta_form.nombreReceta.data
        descripcion = receta_form.descripcion.data
        insumos = request.form.getlist('insumo[]')
        cantidades = request.form.getlist('cantidad[]')
        unidades = request.form.getlist('unidad[]')
        
        # Armar ingredientes
        ingredientes = [
            {'insumo': i, 'cantidad': c, 'unidad': u}
            for i, c, u in zip(insumos, cantidades, unidades)
            if i and c and u
        ]
        
        
        nueva_receta = Receta(
            nombreReceta=nombre,
            Descripccion=descripcion, 
            ingredientes=ingredientes,
            estatus=1
        )
        
        db.session.add(nueva_receta)
        db.session.commit()
        
        flash("Receta agregada correctamente", "success")
        return redirect(url_for('recetas'))

    receta = Receta.query.filter_by(estatus=1).all()
    return render_template('recetas.html', form=receta_form, receta=receta)

@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    if request.method == 'GET':
        idReceta = request.args.get('idReceta')
        receta = db.session.query(Receta).filter(Receta.idReceta == idReceta).first()
        
        if receta:
            receta.estatus = 0
            db.session.commit()
            flash("Receta desactivada correctamente", "success")
        else:
            flash("Receta no encontrada", "danger")
        
        return redirect(url_for('recetas'))

    return redirect(url_for('recetas'))

@app.route('/modificar', methods=['GET', 'POST'])
def modificar():
    idReceta = request.args.get('idReceta')  # Obtener el idReceta de la query string
    if idReceta:
        receta_form = forms.RecetaForm(request.form)

        if request.method == 'POST' and receta_form.validate():
            nombre = receta_form.nombreReceta.data
            descripcion = receta_form.descripcion.data
            insumos = request.form.getlist('insumo[]')
            cantidades = request.form.getlist('cantidad[]')
            unidades = request.form.getlist('unidad[]')

            # Armar ingredientes
            ingredientes = [
                {'insumo': i, 'cantidad': c, 'unidad': u}
                for i, c, u in zip(insumos, cantidades, unidades)
                if i and c and u
            ]

            receta = Receta.query.filter_by(idReceta=idReceta).first()
            if receta:
                receta.nombreReceta = nombre
                receta.Descripccion = descripcion
                receta.ingredientes = ingredientes
                db.session.commit()

                flash("Receta actualizada correctamente", "success")
                return redirect(url_for('recetas'))


        receta = Receta.query.filter_by(idReceta=idReceta).first()
        if receta:
            receta_form.nombreReceta.data = receta.nombreReceta
            receta_form.descripcion.data = receta.Descripccion

        return render_template('modificar_receta.html', form=receta_form, idReceta=idReceta, receta=receta)
    else:
        flash("Receta no encontrada", "danger")
        return redirect(url_for('recetas'))


@app.route('/get_receta/<int:idReceta>', methods=['GET'])
def get_receta(idReceta):
    receta = Receta.query.filter_by(idReceta=idReceta).first()
    if receta:
        ingredientes_json = json.dumps(receta.ingredientes)
        return {
            'nombreReceta': receta.nombreReceta,
            'descripcion': receta.Descripccion,
            'ingredientes': ingredientes_json
        }
    else:
        return {'error': 'Receta no encontrada'}, 404





if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
app.run(debug=True, port=5002)