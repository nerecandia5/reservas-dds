from flask import Flask, jsonify,request
from flask_cors import CORS  # Importar CORS
import mysql.connector
from mysql.connector import Error
app = Flask(__name__)

# Habilitar CORS para todas las rutas
CORS(app)

@app.route("/api/pais")
def pais():
    # Configura la conexión
    config = {
        'user': 'reservas',
        'password': 'reservas111',
        'host': '10.9.120.5',
        'database': 'reservastheloft'
    }

    try:
        # Crea la conexión
        conn = mysql.connector.connect(**config)
        print("Conexión exitosa")

        # Crea un cursor
        cursor = conn.cursor()

        # Ejecuta la consulta SELECT
        cursor.execute("SELECT * FROM Pais")

        # Obtiene los resultados y los nombres de las columnas
        columnas = [column[0] for column in cursor.description]
        resultados = cursor.fetchall()

        # Convierte las tuplas en diccionarios
        lista = [dict(zip(columnas, fila)) for fila in resultados]

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": str(err)}), 500
    finally:
        # Cierra el cursor y la conexión
        try:
            cursor.close()
            conn.close()
        except:
            pass  # No hacer nada si el cierre falla

    return jsonify(lista)  # Devuelve la lista como JSON




@app.route("/api/establecimientos")
def establecimientos():
    
    config = {
    'user': 'reservas',
    'password': 'reservas111',
    'host': '10.9.120.5',
    'database': 'reservastheloft'
}

    try:
         # Crea la conexión
        conn = mysql.connector.connect(**config)
        print("Conexión exitosa")

        # Crea un cursor
        cursor = conn.cursor()

        # Consulta para obtener el establecimiento por ID
        query = "SELECT * FROM Establecimientos"
        cursor.execute(query)
        establecimiento = cursor.fetchall()

        cursor.close()

    except Error as e:
        return jsonify({"error": str(e)}), 500

    if establecimiento:
        return jsonify(establecimiento)
    else:
        return jsonify({"error": "Establecimiento no encontrado"}), 404

# Iniciar la aplicación
app.run(debug=True)





@app.route("/api/establecimientos/<int:id>", methods=['GET'])
def obtener_establecimiento(id):
    
        # Configuración de la base de datos
    config = {
    'user': 'reservas',
    'password': 'reservas111',
    'host': '10.9.120.5',
    'database': 'reservastheloft'
}
    try:
         # Crea la conexión
        conn = mysql.connector.connect(**config)
        print("Conexión exitosa")

        # Crea un cursor
        cursor = conn.cursor()
            # Consulta para obtener el establecimiento por ID
        query = "SELECT * FROM establecimientos WHERE id = %s"
        cursor.execute(query, (id,))
        establecimiento = cursor.fetchone()

        cursor.close()

    except Error as e:
        return jsonify({"error": str(e)}), 500


    if establecimiento:
        return jsonify(establecimiento)
    else:
        return jsonify({"error": "Establecimiento no encontrado"}), 404

# Iniciar la aplicación
app.run(debug=True)


from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# Configuración de la base de datos
config = {
    'user': 'reservas',
    'password': 'reservas111',
    'host': '10.9.120.5',
    'database': 'reservastheloft'
}

@app.route("/api/establecimientos/<int:id>", methods=['DELETE'])
def eliminar_establecimiento(id):
    try:
        # Crea la conexión
        conn = mysql.connector.connect(**config)
        print("Conexión exitosa")

        # Crea un cursor
        cursor = conn.cursor()

        # Consulta para eliminar el establecimiento por ID
        query = "DELETE FROM establecimientos WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()  # Confirma la transacción

        # Verifica si se eliminó algún registro
        if cursor.rowcount > 0:
            return jsonify({"message": "Establecimiento eliminado exitosamente"}), 200
        else:
            return jsonify({"error": "Establecimiento no encontrado"}), 404

    except Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()  # Cierra la conexión

# Iniciar la aplicación
app.run(debug=True)


from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# Configuración de la base de datos
config = {
    'user': 'reservas',
    'password': 'reservas111',
    'host': '10.9.120.5',
    'database': 'reservastheloft'
}

@app.route("/api/establecimientos/<int:id>", methods=['DELETE'])
def eliminar_establecimiento(id):
    try:
        # Crea la conexión
        conn = mysql.connector.connect(**config)
        print("Conexión exitosa")

        # Crea un cursor
        cursor = conn.cursor()

        # Consulta para eliminar el establecimiento por ID
        query = "DELETE FROM Establecimientos WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()  # Confirma la transacción

        # Verifica si se eliminó algún registro
        if cursor.rowcount > 0:
            return jsonify({"message": "Establecimiento eliminado exitosamente"}), 200
        else:
            return jsonify({"error": "Establecimiento no encontrado"}), 404

    except Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()  # Cierra la conexión

@app.route("/api/pais", methods=['POST'])
def insertar_pais():
    data = request.get_json()  # Obtener los datos del cuerpo de la solicitud
    nombre = data.get('Nombre')

    if not nombre:
        return jsonify({"error": "El nombre del país es requerido"}), 400

    try:
        # Crea la conexión
        conn = mysql.connector.connect(**config)
        print("Conexión exitosa")

        # Crea un cursor
        cursor = conn.cursor()

        # Consulta para insertar un nuevo país
        query = "INSERT INTO Pais (Nombre) VALUES (%s)"
        cursor.execute(query, (nombre,))
        conn.commit()  # Confirma la transacción

        return jsonify({"message": "País insertado exitosamente", "id": cursor.lastrowid}), 201

    except Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()  # Cierra la conexión

# Iniciar la aplicación
app.run(debug=True)


