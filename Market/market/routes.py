from flask import Flask,render_template, redirect, url_for
from market import app # No se importa desde __init__ porque, aparentemente, también se puede importar desde un paquete, en este caso, market
from market.models import item, User
from market.forms import RegisterForm
from market import db

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

@app.route("/register" ,methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        with app.app_context():
            db.session.add(user_to_create)
            db.session.commit()
            return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            print(f'There was an error with creating a user: {err_msg}')
    return render_template('register.html',form=form)
