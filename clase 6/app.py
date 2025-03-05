# Importar la librería de Flask
from flask import Flask, render_template, request
# Importar la librería de MongoDB
from pymongo import MongoClient


# Crear instancia de Flask
app = Flask(__name__)

# Crear un cliente de Mongo
cliente = MongoClient("mongodb+srv://santiagosilvabl:etpbAiSqf9VO0Js5@curso.blhee.mongodb.net/")
# Llamar a la base de datos - diccionario
app.db = cliente.ejemplo

# Recorrer los usuarios registrados en la DB
usuarios = [usuario for usuario in app.db.usuarios.find({})]
print(usuarios)


# Ruta de acceso al Formulario. Para poderse ejecutar el formulario debe cumplir con ambos métodos
@app.route("/home", methods = ["GET", "POST"])
# Función a ejecutar cuando ingrese a la ruta
def home():

    # Obtener la información - Saber si se está enviando información a través de un formulario
    if(request.method == "POST"):
        # Almacenar información solicitada del formulario
        info_formulario = request.form.get("contenido")
        # Almacenar la información del formulario en el diccionario para poder guardarla en la DB
        parametros = {"nombre" : info_formulario}
        # Añadir el contenido capturado del formulario a la lista con formato de diccionario
        usuarios.append(parametros)
        # Guardar los datos en la colección
        app.db.usuarios.insert_one(parametros)

    # Retornar y renderizar template
    return render_template("home.html", usuarios = usuarios)


# Configurar el fichero para que se ejecute siempre como el principal
if __name__ == "__main__":
    app.run()
