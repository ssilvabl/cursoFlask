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

# Definir ruta utilizando el motor de plantillas
@app.route("/primera")
def template_pagina1():
    return render_template("pagina1.html")


# Ruta con plantilla y utilizando variables
@app.route("/segunda")
def template_pagina2():
    return render_template("pagina2.html", num1 = 0, num2 = 0, apellido = "", nombre = "Santiago", curso = "Flask")

# Ruta con plantillas y utilizando variables dentro de la función
@app.route("/tercera")
def template_pagina3():
    num1 = 0
    num2 = 0
    apellido = "hola"
    return render_template("pagina2.html", num1 = num1, num2 = num2, apellido = apellido, nombre = "Silva", curso = "Python")


# Ruta con plantillas y utilizando operaciones artiméticas
@app.route("/operaciones")
def template_pagina4():
    return render_template("pagina2.html", num1 = 10, num2 = 20, apellido = "silva")


# Ruta con plantillas y diccionario con variables
@app.route("/diccionario")
def template_pagina5():
    # Diccionario con variables a enviar al template
    kwargs = {
        "num1" : 10,
        "num2" : 20,
        "apellido" : "diccionario"

    }

    # Renderizar el template con el diccionario como parámetros
    return render_template("pagina2.html", **kwargs)



# Validar si el script se está ejecutando directamente desde el programa principal
if __name__ == "__main__":
    app.run()
