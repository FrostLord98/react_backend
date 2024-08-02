from flask import Flask,request
from dotenv import load_dotenv
from flask_cors import CORS
from os import getenv
from psycopg import connect

app = Flask(__name__)
CORS(app)


load_dotenv('C:/Users/frost/Desktop/ultimo hack js/app/src/backend/.env')

app.config["AWS_ACCESS_KEY_ID"] = process.env.("AWS_ACCESS_KEY_ID")
app.config["AWS_SECRET_KEY_ID"] = process.env.("AWS_SECRET_KEY_ID")


def connect_to_db():
    conn = connect(
    host = process.env.("DB_HOST"),
    user = process.env.("DB_USER"),
    password = process.env.("DB_PASSWORD"),
    dbname = process.env.("DB_NAME"),
    
    )
    return conn


@app.route("/nombres")
def get_nombres():
    nombres = []
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute('select nombre from usuarios')
    user = cursor.fetchall()
    connection.close()
    for i in user:
        nombres.append(i[0])

    return nombres
@app.route("/correos")
def get_correos():
    correos = []
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute('select correo from usuarios')
    user = cursor.fetchall()
    connection.close()
    for i in user:
        correos.append(i[0])

    return correos
@app.route("/edades")
def get_edades():
    edades = []
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute('select edad from usuarios')
    user = cursor.fetchall()
    connection.close()
    for i in user:
        edades.append(i[0])

    return edades

@app.route("/agregar",methods=["POST"])
def agregar_usuario():
    edad = request.form['edad']
    nombre = request.form['nombre']
    correo = request.form['correo']

    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute('insert into usuarios(edad,nombre,correo) values(%s,%s,%s)',(edad,nombre,correo))
    connection.commit()
    connection.close()
    return 201

@app.route("/borrar",methods=["put"])
def borrar_usuario():
    nombre = request.form['nombre']

    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute('delete from usuarios where nombre = %s',(nombre,))
    connection.commit()
    connection.close()
    return 200

@app.route("/modificarCorreo",methods=["put"])
def modificar_correo():
    nombre = request.form['nombre']
    correo = request.form['correo']

    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute('update usuarios set correo = %s where nombre = %s',(correo,nombre))
    connection.commit()
    connection.close()
    return 200

@app.route("/modificarNombre",methods=["put"])
def modificar_nombre():
    nombre = request.form['nombre']
    correo = request.form['correo']

    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute('update usuarios set nombre = %s where correo = %s',(nombre,correo,))
    connection.commit()
    connection.close()



if __name__ == "__main__":
    app.run(debug=True)
