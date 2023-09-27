from random import randint, choice as rc
from faker import Faker
from models import db, Restaurant, Pizza, RestaurantPizzas
from app import app

fake = Faker()


with app.app_context():
    Restaurant.query.delete()
    Pizza.query.delete()

    restaurants = []
    for i in range(50):
        restaurant = Restaurant(
          name= fake.name(),
          super_name = fake.first_name(),  
        )
        restaurants.append(restaurant)
    db.session.add_all(restaurants)

    pizzas = []
    for i in range(50):
        pizza = Pizza(
            name = fake.name(),
            description = fake.paragraph()
        )
        pizzas.append(pizza)
    db.session.add_all(pizzas)

    

    # combinations = set()
    # price = ["15", "23", "30"]
    # RestaurantPizzas = []
    # for _ in range(50):
    #     RestaurantPizzas = RestaurantPizzas
    #     restaurants_id = randint(1, 50)
    #     Pizza_id = randint(1, 50)
    #     price = rc(price)

    #     if (restaurants_id, Pizza_id, price) in combinations:
    #         continue
    #     combinations.add((restaurants_id, Pizza_id, price))
    #     RestaurantPizzas_data = {"restaurants_id": restaurants_id, "Pizza_id": Pizza_id, "price": price}
    #     statement = db.insert(RestaurantPizzas).values(RestaurantPizzas_data)
        # db.session.execute(statement)
        # db.session.commit()
    db.session.commit()