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

    def __repr__(self): # Este método sirve para que, en la terminal, aparezcan los nombres de los items en lugar de un número
        return f"Item {self.name}"

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
    items = item.query.all() # Este método selecciona todos los items de la tabla y los guarda en la variable
    
    return render_template("market.html", items=items)
