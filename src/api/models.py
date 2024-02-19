from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


# nuestra clase Product donde definimos todo lo necesario para mostrar en la pagina, incluyendo el nuevo agregado descuento
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(50), nullable=False)
    discount = db.Column(db.Float, nullable=True, default=0.0)  #Asegurarse de que el valor introducido sea un float x ejemplo 0.20 = 20% de descuento

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "image_url": self.image_url,
            "description": self.description,
            "category": self.category,
            "discount": self.discount,

        }