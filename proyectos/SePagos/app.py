# Importar Flask
# render_template para trabajar con el motor de plantillas jinja2
# request para trabajar con solicitudes get y post
from flask import Flask, render_template, request
# Importar módulo de la conexión a la base de datos
import database as db


# Crar la aplicación de Flask
app = Flask(__name__)

cursor = db.database.cursor() # Cursor/Controlador para ejecutar consultas SQL en la DB

# DEFINIR RUTAS

# Ruta Principal y función a devolver
@app.route('/')
# Función a ejecutar
def home():
    # Instrucciones

    # Retornar vista HTML con el motor de plantillas jinja2
    # R¿render_template le indica a flask que busque el archivo mencionado en la carpeta templates y lo muestre
    return render_template('index.html')

# Ruta de Pagos
@app.route('/cobrar')
# Función a ejecutar
def payments():
    # Instrucciones

    # Ejecutar consulta en la DB
    cursor.execute("SELECT * FROM payments")
    # Recuperar resultado de la consulta a la DB
    list_payments = cursor.fetchall()

    # Retornar vista HTML
    return render_template('payments.html', list_payments = list_payments)

# Ruta para Añadir Pagos
@app.route('/nuevoPago', methods=['GET', 'POST'])
def newPayment():
    # Instrucciones

    # Mensaje de confirmación
    msg = ''
    # Validar si el formulario se envió mediante la solicitud del método POST
    if request.method == 'POST':
        # Si se envió con el método POST

        # Capturar datos del formulario (utilizando el selecctor name de HTML)
        nombre_pago = request.form.get('nombrePago')
        monto_inicial = request.form.get('montoInicial')
        numero_cuotas = request.form.get('numeroCuotas')
        fecha_inicio = request.form.get('fechaInicio')
        fecha_fin = request.form.get('fechaFin')

        # Insertar registro en la DB
        cursor.execute("INSERT INTO payments (name, amount, installments, date_start, date_end) VALUES (%s, %s, %s, %s, %s)",
                       (nombre_pago,
                       monto_inicial,
                       numero_cuotas,
                       fecha_inicio,
                       fecha_fin))
        # Confirmar y Guardar los datos de forma permanente en la base de datos
        db.database.commit()
        # Mensaje de confirmación
        msg = '¡El registro se guardó de forma correcta!'
        

    # Retornar vista HTML
    return render_template('newPayment.html', msg = msg)

# Ruta de Detalles del Pago
@app.route('/cobrar/<id>')
def paymentDetails(id):
    # Instrucciones

    # Convertir ID en int
    id = int(id)
    # Ejecutar consulta SQL en la DB
    cursor.execute(f"SELECT * FROM payments WHERE id = {id}")
    # Obtener resultado de la consulta SQL
    details = cursor.fetchall()

    # Retornar vista HTML y datos
    return render_template('paymentDetails.html', pago = id, details = details)

# Ruta de la Lista de Ayudas
@app.route('/ayuda')
def help():

    # Renderizar vista en el navegador
    return render_template('help.html')

# Ruta de Ayuda con parámetros
@app.route('/ayuda/<id>')
def helpDetails(id):

    # Retornar vista y enviar valor de la variable id
    return render_template('helpDetails.html', guia = id)

# Ruta del Perfil utilizando el método get y post
# El método get se utiliza para consultas o búsquedas
# El método post se utiliza para enviar datos de forma interna, es más seguro
@app.route('/registro', methods=['GET', 'POST'])
def register():
    # Instrucciones
    # Inicializar la variable name sin ningún valor
    name = None

    # Validar si el formulario se envió mediante la solicitud del método POST
    if request.method == 'POST':
        # Si es así, se captura el dato del campo en el formulario (utilizando el selecctor name de HTML)
        # En caso de que el método sea GET, se capturan los datos con request.args.get('name')
        name = request.form.get('nombre')

    # Retornar vista y datos capturados del formulario
    return render_template('register.html', name = name)

# Ruta de los Usuarios registrados
@app.route('/usuarios')
def users():

    # Enviar solo la consulta SQL a la base de datos
    cursor.execute("SELECT id, name, password, email FROM users")
    # Obtener el resultado de la consulta SQL enviada a la DB en una lista de tuplas (cada tupla es un registro)
    list_users = cursor.fetchall()

    return list_users


# Ejecutar la aplicación si este archivo es el principal
if __name__ == '__main__':
    # Ejecutar la app
    app.run(debug=True)
