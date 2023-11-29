from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL


app = Flask(__name__)



app.secret_key = 'your_secret_key'

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "surya@93452"
app.config["MYSQL_DB"] = "face_recognition"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    con = mysql.connection.cursor()
    sql = "SELECT * from attendance"
    con.execute(sql)
    res = con.fetchall()
    return render_template('home.html', datas=res)
    

@app.route('/truncate_table', methods=['POST'])
def truncate_table():
    con = mysql.connection.cursor()
    con.execute("TRUNCATE TABLE attendance")
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/validate', methods=['GET', 'POST'])
def validate():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']

        con = mysql.connection.cursor()
        sql = "SELECT * FROM login WHERE email=%s AND password=%s"
        con.execute(sql, (email, password))
        user = con.fetchone()

        if user:
            session['email'] = user['email']
            return redirect(url_for('home'))
        else:
            error = 'Invalid login credentials'
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
