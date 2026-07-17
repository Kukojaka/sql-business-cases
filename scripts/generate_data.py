from faker import Faker
import pandas as pd
import random
from pathlib import Path

fake = Faker()

random.seed(42)
Faker.seed(42)

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "datasets"
DATASET_DIR.mkdir(exist_ok=True)

cities = [
    "London",
    "Berlin",
    "Paris",
    "Amsterdam",
    "Madrid",
    "Rome",
    "Vienna",
    "Prague"
]

products = [
    ("iPhone 15", "Smartphones", 999),
    ("Galaxy S24", "Smartphones", 899),
    ("Google Pixel 9", "Smartphones", 799),
    ("MacBook Air M3", "Laptops", 1299),
    ("Dell XPS 13", "Laptops", 1199),
    ("Lenovo ThinkPad X1", "Laptops", 1399),
    ("Sony WH-1000XM5", "Audio", 399),
    ("AirPods Pro 2", "Audio", 249),
    ("JBL Charge 5", "Audio", 179),
    ("Apple Watch Series 10", "Wearables", 499),
    ("Galaxy Watch 7", "Wearables", 429),
    ("iPad Air", "Tablets", 699),
    ("Kindle Paperwhite", "Tablets", 189),
    ("PlayStation 5", "Gaming", 549),
    ("Xbox Series X", "Gaming", 549)
]
