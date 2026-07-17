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