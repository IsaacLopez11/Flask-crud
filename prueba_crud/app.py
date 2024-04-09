from flask import Flask, request , redirect ,render_template, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'secretkey'


app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "flask"


mysql = MySQL(app)


@app.route('/registrar', methods=['POST'])
def registrar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO clientes( nombre, apellidos, correo) VALUES (%s,%s,%s)',
                    (nombre, apellido, correo)
                    )

        mysql.connection.commit()
        flash("Usuario Guardado satisfactoriamente")

    return redirect('/formulario')



@app.route('/')
def hello():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM clientes")
    data = cur.fetchall()

    return render_template('index.html', clientes=data )



@app.route('/formulario')
def form():
    
    return render_template('formulario.html' )


if __name__ == '__main__':
    app.run(debug=True)

