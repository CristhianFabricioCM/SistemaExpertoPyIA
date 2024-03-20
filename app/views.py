from flask import render_template, request, jsonify
from app import app
from app.models import Usuario

@app.route('/')
def index():
    usuario = Usuario(nombre='Grupo IA 3')
    return render_template('index.html', usuario=usuario)

# Nueva ruta para la suma
@app.route('/sumar', methods=['POST'])
def sumar():
    if request.method == 'POST':
        numero1 = float(request.form.get('numero1', 0))
        numero2 = float(request.form.get('numero2', 0))
        resultado = numero1 + numero2
        return jsonify({'resultado': resultado})