# Importar Flask
from flask import Flask, render_template


# Instancia de Flask
app = Flask(__name__)

# Ruta para el buble For
@app.route("/loop-for")
# Función a ejecutar cuando se ingrese a la ruta
def loop_for():
    
    # Lista con elementos a enviar a la plantilla
    paises = [
        "Colombia",
        "Venezuela",
        "México",
        "Ecuador"
    ]

    # Retornar y renderizar la plantilla
    return render_template("home.html")


# Configurar las opciones para realizar la ejecución como fichero principal
if __name__ == "__main__":
    app.run()
