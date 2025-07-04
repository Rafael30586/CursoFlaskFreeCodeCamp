from market import db
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50),nullable=False, unique=True)
    password_hash = db.Column(db.String(length=50),nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('item', backref='owned_user', lazy=True)

class item(db.Model): # Esta clase será mapeada a una tabla de una base de datos, ya que sqlalchemy es un ORM 
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(),nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=200), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self): # Este método sirve para que, en la terminal, aparezcan los nombres de los items en lugar de un número
        return f"Item {self.name}"
