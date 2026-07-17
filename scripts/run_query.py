import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "database" / "store.db"
QUERY_PATH = BASE_DIR / "solutions" / "top_10_products.sql"

conn = sqlite3.connect(DB_PATH)

with open(QUERY_PATH, "r") as file:
    query = file.read()

cursor = conn.cursor()

cursor.execute(query)

results = cursor.fetchall()

print("Количество строк:", len(results))

for row in results:
    print(row)

conn.close()