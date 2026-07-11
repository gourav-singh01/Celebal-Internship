import sqlite3
import pandas as pd

conn = sqlite3.connect("database/ecommerce.db")
cursor = conn.cursor()

with open("sql/schema.sql", "r") as f:
    cursor.executescript(f.read())

customers = pd.read_csv("data/cleaned/customers_clean.csv")
products = pd.read_csv("data/cleaned/products_clean.csv")
orders = pd.read_csv("data/cleaned/orders_clean.csv")
order_items = pd.read_csv("data/cleaned/order_items_clean.csv")

customers.to_sql("customers", conn, if_exists="append", index=False)
products.to_sql("products", conn, if_exists="append", index=False)
orders.to_sql("orders", conn, if_exists="append", index=False)
order_items.to_sql("order_items", conn, if_exists="append", index=False)

print("Database loaded successfully.")

print("\nRow Counts")
print("Customers :", len(customers))
print("Products  :", len(products))
print("Orders    :", len(orders))
print("Items     :", len(order_items))

conn.close()