from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['userName']
    password = request.form['pswd']
    captcha_response = request.form['g-recaptcha-response']

    # Verificar el CAPTCHA con Google
    secret_key = '6Lfzv_gqAAAAALxgoUOobpOFldn0VikXsHcuoGRl'  # Inserta tu Clave secreta aquí
    verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    response = requests.post(verify_url, data={
        'secret': secret_key,
        'response': captcha_response
    })
    result = response.json()

    if result.get('success'):
        # Si el CAPTCHA es válido, procesa el inicio de sesión
        if username == "usuario" and password == "contraseña":  # Ejemplo básico de autenticación
            return "¡Inicio de sesión exitoso!"
        else:
            return "Usuario o contraseña incorrectos."
    else:
        return "Por favor, verifica que no eres un robot."

if __name__ == '__main__':
    app.run(debug=True, port=3000)