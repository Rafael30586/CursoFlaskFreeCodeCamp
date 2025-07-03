from market import db


class item(db.Model): # Esta clase será mapeada a una tabla de una base de datos, ya que sqlalchemy es un ORM 
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(),nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=200), nullable=False, unique=True)

    def __repr__(self): # Este método sirve para que, en la terminal, aparezcan los nombres de los items en lugar de un número
        return f"Item {self.name}"
