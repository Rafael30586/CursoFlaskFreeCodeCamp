from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rafael@localhost:3306/market' # Tuve que instalar el driver pymysql para que acepte esta uri, ya que, al parecer trabaja con SQLlite por defecto
app.config['SECRET_KEY'] = '966d55038995bc7582a7a412'
db = SQLAlchemy(app)

from market import routes

# db.init_app(app)
#@app.route("/") # Esto es un decorador
#def hello_world():
#    return "<h1>Hello world</h1>"


#with app.app_context(): Esto permitió que se creara la base de datos. En la terminal se me exigía el application context
 #   db.create_all()

