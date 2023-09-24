from random import randint, choice as rc
from faker import Faker
from models import db, Restaurant, Pizza, Restaurant_pizzas
from app import app

fake = Faker()