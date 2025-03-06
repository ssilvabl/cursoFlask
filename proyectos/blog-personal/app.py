# Importar Flask
from flask import Flask, render_template, request
# Importar Datetime para trabajar con fechas
import datetime
# Importar MongoDB
from pymongo import MongoClient


# Crear instancia de Flask
app = Flask(__name__)
# Crear cliente de Mongo
cliente = MongoClient("mongodb+srv://santiagosilvabl:etpbAiSqf9VO0Js5@curso.blhee.mongodb.net/")
# Acceder a la DB
app.db = cliente.blog

# Lista para Almacenar las entradas
#entradas = []
# Recorrer entradas de la DB
entradas = [entrada for entrada in app.db.contenido.find({})]
print(entradas)

# Crear ruta inicial y utilizar los 2 métodos
@app.route("/", methods = ["GET", "POST"])
# Función a ejecutar cuando se ingrese a la ruta
def home():
    # Validar si recibimos respuesta del tipo POST
    if(request.method == "POST"):
        # Si se recibe la respuesta se almacenan los datos del formulario
        # Se identifica el input con el name que tiene en el HTML
        titulo = request.form.get("title") # -> Se obtiene el título
        descripcion = request.form.get("description") # -> Se obtiene la descripción
        fecha_registro = datetime.datetime.today().strftime("%d-%m-%Y") # -> Obtener la fecha actual del registro

        # Guardar toda la información en un diccionario
        datos_formulario = {"titulo" : titulo, "descripcion" : descripcion, "fecha" : fecha_registro}
        # Agregar diccionario a la lista
        entradas.append(datos_formulario)
        # Guardar los datos del formulario en la DB
        app.db.contenido.insert_one(datos_formulario)

    return render_template("home.html", entradas = entradas)



# Configurar el fichero para que se ejecute como principal
if __name__ == "__main__":
    app.run()
