# Importar Flask
from flask import Flask, render_template


# Crear una instancia de Flask
app = Flask(__name__)

# Ruta para Condicionales
@app.route("/condicionales")
# Función a ejecutar cuando se ingrese a la ruta
def condicionales():
    # Retornar y renderizar vista
    return render_template("home.html", pais = "Vene")



# Configurar el fichero para que se ejecute como de forma directa como el principal
if __name__ == "__main__":
    app.run()
