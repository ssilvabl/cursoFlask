# Importar la librería de Flask
from flask import Flask, render_template, request


# Crear instancia de Flask
app = Flask(__name__)


# Ruta de acceso al Formulario. Para poderse ejecutar el formulario debe cumplir con ambos métodos
@app.route("/home", methods = ["GET", "POST"])
# Función a ejecutar cuando ingrese a la ruta
def home():

    # Variable para almacenar la información del formulario
    info_formulario = ""

    # Obtener la información - Saber si se está enviando información a través de un formulario
    if(request.method == "POST"):
        # Almacenar información solicitada del formulario
        info_formulario = request.form.get("contenido")

    # Retornar y renderizar template
    return render_template("home.html", nombre = info_formulario)


# Configurar el fichero para que se ejecute siempre como el principal
if __name__ == "__main__":
    app.run()
