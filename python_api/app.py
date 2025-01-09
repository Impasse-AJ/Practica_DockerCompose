import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hola')
def saludo_generico():
    return jsonify({"mensaje": "¡Hola, mundo!"})

@app.route('/hola/<nombre>')
def saludo_personalizado(nombre):
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})

if __name__ == '__main__':
    # Obtener puerto del entorno o usar 5000 por defecto
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
