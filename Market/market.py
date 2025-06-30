from flask import Flask, render_template
app = Flask(__name__)

#@app.route("/") # Esto es un decorador
#def hello_world():
#    return "<h1>Hello world</h1>"

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
