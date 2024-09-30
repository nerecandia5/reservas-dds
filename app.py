from flask import Flask, jsonify
import flask
import mysql.connector

app = flask(__name__)

@app.route("/pais")
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
    finally:
        # Cierra el cursor y la conexión
        cursor.close()
        conn.close()

    return jsonify(resultados)
