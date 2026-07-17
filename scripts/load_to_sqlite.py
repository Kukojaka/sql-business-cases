from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "datasets"
DATABASE_DIR = BASE_DIR / "database"

DB_PATH = DATABASE_DIR / "store.db"

conn = sqlite3.connect(DB_PATH)

files = [
    "customers",
    "products",
    "orders",
    "order_items"
]

for file in files:
    df = pd.read_csv(DATASET_DIR / f"{file}.csv")

    df.to_sql(
        file,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"{file} table created")

conn.close()

print("Database created:", DB_PATH)