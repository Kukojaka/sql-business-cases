from pathlib import Path

import pandas as pd
from faker import Faker
import random

random.seed(42)
Faker.seed(42)

fake = Faker()

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "datasets"

print(DATASET_DIR)

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

customers = []

for customer_id in range(1, 101):
    customers.append({
        "customer_id": customer_id,
        "full_name": fake.name(),
        "city": random.choice(cities),
        "registration_date": fake.date_between(
            start_date="-3y",
            end_date="-30d"
        )
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    DATASET_DIR / "customers.csv",
    index=False
)

print("✅ customers.csv created")

products_data = []

for product_id, product in enumerate(products, start=1):
    products_data.append({
        "product_id": product_id,
        "product_name": product[0],
        "category": product[1],
        "price": product[2]
    })

products_df = pd.DataFrame(products_data)

products_df.to_csv(
    DATASET_DIR / "products.csv",
    index=False
)

print("products.csv created")

orders = []

for order_id in range(1, 501):
    orders.append({
        "order_id": order_id,
        "customer_id": random.randint(1, 100),
        "order_date": fake.date_between(
            start_date="-1y",
            end_date="today"
        )
    })

orders_df = pd.DataFrame(orders)

orders_df.to_csv(
    DATASET_DIR / "orders.csv",
    index=False
)

print("orders.csv created")

order_items = []

for order_id in range(1, 501):
    items_count = random.randint(1, 5)

    for _ in range(items_count):
        order_items.append({
            "order_id": order_id,
            "product_id": random.randint(1, len(products)),
            "quantity": random.randint(1, 3)
        })

order_items_df = pd.DataFrame(order_items)

order_items_df.to_csv(
    DATASET_DIR / "order_items.csv",
    index=False
)

print("order_items.csv created")