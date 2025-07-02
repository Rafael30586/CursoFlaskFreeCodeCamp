from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rafael@localhost:3306/market' # Tuve que instalar el driver pymysql para que acepte esta uri, ya que, al parecer trabaja con SQLlite por defecto
db = SQLAlchemy(app)

# db.init_app(app)
#@app.route("/") # Esto es un decorador
#def hello_world():
#    return "<h1>Hello world</h1>"

class item(db.Model): # Esta clase será mapeada a una tabla de una base de datos, ya que sqlalchemy es un ORM 
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(),nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=200), nullable=False, unique=True)

with app.app_context():
    db.create_all()

@app.route("/about/<username>") 
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'

@app.route("/home-page") # Se le puede poner dos rutas a un mismo método
@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/market")
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': 5986040, 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': 9583040, 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': 59201940, 'price': 150}
    ]
    
    
    return render_template("market.html", items=items)
