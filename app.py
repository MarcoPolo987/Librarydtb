from flask import Flask,render_template,request
from flaskext.mysql import MySQL

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
app.config['MYSQL_DATABASE_URI'] = 'mysql://root:password123@localhost/users'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkout',methods=['GET','POST'])
def checkout():
    cur = mysql.connection.cursor()
    users = cur.execute("SELECT * FROM users")
    if(users>0):
        userDetails = cur.fetchall()
    return render_template('checkout.html')

@app.route('/catalogue')
def catalogue():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSER INTO users (username, password) VALUES(%s,%s)", (username,password))
        mysql.connection.commit()
        cur.close()
        return "success"
    return render_template('catalogue.html')


@app.route('/userlogin')
def userlogin():
    return render_template('userlogin.html')

if(__name__ == "__main__"):
    app.run(debug=True)

