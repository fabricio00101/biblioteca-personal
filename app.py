from flask import Flask, render_template, jsonify, request
import mysql.connector

app = Flask(__name__)

db_config ={
    'user': 'root',
    'password': '43110918',
    'host': '127.0.0.1',
    'database': 'biblioteca_personal'

}

@app.route("/")
def index():
    libros= []
    total_libros = 0
    conn = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT
                L.id_libro,
                L.titulo, 
                A.nombre AS autor, 
                L.anio_publicacion,
                L.leido
            FROM 
                Libros AS L
            JOIN 
                Libros_Autores AS LA ON L.id_libro = LA.id_libro
            JOIN    
                Autores AS A ON LA.id_autor = A.id_autor
            ORDER BY 
                L.titulo;
        """
        cursor.execute(query)
        libros=cursor.fetchall()
        total_libros = len(libros)

    except mysql.connector.Error as err:
        print(f"Errror: {err}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

    return render_template('index.html', libros = libros, total_libros = total_libros)


@app.route('/alternar_leido/<int:id_libro>', methods=['POST'])
def alternar_leido(id_libro):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("SELECT leido FROM Libros WHERE id_libro =%s", (id_libro,))
        resultado = cursor.fetchone()

        if resultado:
            estado_actual = resultado[0]
            nuevo_estado = not estado_actual

            cursor.execute("UPDATE Libros SET leido = %s WHERE id_libro = %s", (nuevo_estado, id_libro))
            conn.commit()

            return jsonify({'exito': True, 'nuevo_estado': nuevo_estado})
    except mysql.connector.Error as err:
        print (f"Error: {err}")
        return jsonify({'exito': False})
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
if __name__ == "__main__":
    app.run(debug=True)
