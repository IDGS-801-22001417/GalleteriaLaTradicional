from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField
from wtforms import validators

class RecetaForm(FlaskForm):
    nombreReceta = StringField("Nombre de la receta", [
        validators.DataRequired(message="El campo es requerido")
    ])
    descripcion = TextAreaField("Descripción de la receta", [
        validators.DataRequired(message="El campo es requerido")
    ])
    ingredientes = HiddenField()