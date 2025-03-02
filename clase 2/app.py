# Importar Flask
from flask import Flask, render_template

# Crear instancia de Flask
app = Flask(__name__)

# Clase para la película
class Pelicula:
    # Definir su constructor(siempre debe ir)
    def __init__(self, nombre, año, autor):
        # Atributos
        self.nombre = nombre,
        self.año = año,
        self.autor = autor


# Configurar ruta principal
@app.route("/")
# Función a ejecutar cuando se ingrese a la ruta
def raiz():
    # Lista con los datos a enviar al template
    peliculas = [
        "Rambo",
        "Iron man",
        "Thor"
    ]

    # Diccionario con los datos a enviar al template
    detalles = {
        "nombre" : "Iron Man",
        "año" : 2008,
        "autor" : "James Cameron"
    }

    # Crear objeto de la clase Película
    iron = Pelicula("Iron man", 2008, "James Cameron")

    # Retornar y renderizar el template
    return render_template("home.html", movies = peliculas, details = detalles, favorite = iron)


# Configurar el fichero para que se ejecute directamente desde el archivo principal
if __name__ == "__main__":
    app.run()
