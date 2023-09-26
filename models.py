from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()


RestaurantPizzas = db.Table(
    "restaurant_pizzas",
    db.Column("restaurant_id", db.ForeignKey("restaurants.id"), primary_key=True),
    db.Column("pizza_id", db.ForeignKey("pizzas.id"), primary_key=True),
    db.Column("price", db.String),
    db.Column("created_at", db.DateTime, server_default=db.func.now()),
    db.Column("updated_at", db.DateTime, onupdate=db.func.now())
)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    super_name= db.Column(db.String)
    created_at= db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    pizzas = db.relationship("Pizza", secondary=RestaurantPizzas, back_populates="restaurants")
    serialize_rules = ("-Pizza.Restaurants",)

    def __repr__(self):
        return f"Restaurants {self.name} has {self.super_name}."
    

class Pizza(db.Model, SerializerMixin):
    __tablename__ = "pizzas"

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    description= db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    restaurants = db.relationship("Restaurant", secondary=RestaurantPizzas, back_populates="pizzas")
    serialize_rules = ("-Restaurant.pizza",)

    def __repr__(self):
        return f"Pizza {self.name} was created at {self.created_at}."