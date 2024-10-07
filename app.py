from flask import Flask, jsonify
from flask_cors import CORS  # Importar CORS
import mysql.connector

app = Flask(__name__)

# Habilitar CORS para todas las rutas
#CORS(app)

@app.route("/api/pais/<int:id>")
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


@app.route("/api/establecimientos/<int:id>")
def detalle_establecimiento(id):
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

        # Ejecuta la consulta SELECT para obtener el establecimiento por ID
        cursor.execute("SELECT * FROM Establecimientos WHERE id = %s", (id,))

        # Obtiene los resultados y los nombres de las columnas
        columnas = [column[0] for column in cursor.description]
        resultado = cursor.fetchone()  # Solo queremos un resultado

        if resultado is None:
            return jsonify({"error": "Establecimiento no encontrado"}), 404

        # Convierte la tupla en un diccionario
        detalle = dict(zip(columnas, resultado))

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

    return jsonify(detalle)  # Devuelve el detalle como JSON




 
