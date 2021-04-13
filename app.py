from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flaskext.mysql import MySQL



app = Flask(__name__)


app.config['MYSQL_DATABASE_HOST'] = 'ec2-54-67-35-76.us-west-1.compute.amazonaws.com'
app.config['MYSQL_DATABASE_PORT'] = 3600
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Filemaker34'
app.config['MYSQL_DATABASE_DB'] = 'db_mysql_sbhx'
mysql = MySQL(app)
mysql.init_app(app)

subscribers = []



@app.route('/')
def index():
    title = 'GAE Portal Home'
    active = "nav-link active"
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM Orders")
    fetchdata = cursor.fetchall()
    cursor.close()
    return render_template('index.html', title=title, fetchdata=fetchdata)

@app.route('/jobs')
def jobs():
    title= 'Jobs Overview'
    active = "nav-link active"
    return render_template('jobs.html', title=title)

@app.route('/customers')
def customers():
    title = 'Customers'
    active = "nav-link active"
    return render_template('customers.html',title=title)

@app.route('/form')
def form():
    title = 'Form'
    active = "nav-link active"
    return render_template('form.html',title=title)

@app.route('/pform', methods=["POST"])
def pform():
    first_name = request.form.get('name_first')
    last_name = request.form.get('name_last')
    email = request.form.get('email')
    subscribers.append(f"{first_name} {last_name} |  {email}" )
    title = 'Form Processing'
    active = "nav-link active"
    errorflag=0
    error_statement = 'All form fields are required'

#Error Handling
    if not first_name or not last_name or not email:
        errorflag =1
        title= 'Form'
        return render_template('form.html',
            title=title, first_name=first_name, last_name=last_name, email=email,subscribers=subscribers, error_statement=error_statement, errorflag=errorflag)
    else:
         return render_template('pform.html',title=title, first_name=first_name, last_name=last_name, email=email, subscribers=subscribers, error_statement=error_statement, errorflag=errorflag)
