from flask import Flask,render_template
from market import app # No se importa desde __init__ porque, aparentemente, también se puede importar desde un paquete, en este caso, market
from market.models import item
from market.forms import RegisterForm

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

@app.route("/register")
def register_page():
    form = RegisterForm()
    return render_template('register.html',form=form)
