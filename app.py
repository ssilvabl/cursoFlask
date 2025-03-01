# Importar Flask
from flask import Flask, render_template

# Crear una instancia de Flask
app = Flask(__name__) # El argumento name representa el nombre del módulo(app.py) que indica donde empieza la raíz del programa

# Definir una ruta o URL donde queremos que se ejecute la función a definir en texto plano
@app.route("/")
def hello_world():
    return "¡Hola, mundo!"

# Definir ruta de Home modificada con HTML
@app.route("/home")
def home():
    return """
        <html>
        
            <body>
                <h1>¡Hola, desde el Home con HTML incrustado!</h1>
            </body>

        </html>
    """

# Definir ruta utilizando plantillas
@app.route("/primera")
def template_pagina1():
    return render_template("pagina1.html")


# Validar si el script se está ejecutando directamente desde el programa principal
if __name__ == "__main__":
    app.run()
