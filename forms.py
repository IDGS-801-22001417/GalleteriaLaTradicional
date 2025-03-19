from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, IntegerField,SubmitField
from wtforms import validators

class UserForm2(Form):
    id_insumo=IntegerField('id_insumo',
    [validators.number_range(min=1, max=20,message='valor no valido')])
    
    nombreInsumo=StringField('nombreInsumo',[
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=3,max=20, message='requiere min=3 max=20')
    ])

    unidad=StringField('unidad',[
        validators.DataRequired(message='El apellido es requerido')
    ])

    total=IntegerField('total',[
        validators.DataRequired(message='El total es requerido')
    ])