import os
import pandas as pd

RAW_PATH = "data/raw"
CLEAN_PATH = "data/cleaned"

os.makedirs(CLEAN_PATH, exist_ok=True)

# -------------------------
# Load Files
# -------------------------

customers = pd.read_csv(f"{RAW_PATH}/customers.csv")
products = pd.read_csv(f"{RAW_PATH}/products.csv")
orders = pd.read_csv(f"{RAW_PATH}/orders.csv")
order_items = pd.read_csv(f"{RAW_PATH}/order_items.csv")

# -------------------------
# Customers
# -------------------------

customers = customers.drop_duplicates(subset="customer_id")

customers["email"] = customers["email"].fillna("unknown@email.com")

customers = customers[
    customers["email"].str.contains("@", na=False)
]

customers["registration_date"] = pd.to_datetime(
    customers["registration_date"],
    errors="coerce"
)

customers = customers.dropna(subset=["registration_date"])

# -------------------------
# Products
# -------------------------

products = products.drop_duplicates(subset="product_id")

products["product_name"] = (
    products["product_name"]
    .str.strip()
    .str.title()
)

# -------------------------
# Orders
# -------------------------

orders = orders.drop_duplicates(subset="order_id")

orders["order_date"] = pd.to_datetime(
    orders["order_date"],
    errors="coerce"
)

orders = orders.dropna(subset=["order_date"])

orders = orders[
    orders["customer_id"].isin(customers["customer_id"])
]

# -------------------------
# Order Items
# -------------------------

order_items = order_items[
    order_items["order_id"].isin(orders["order_id"])
]

order_items = order_items[
    order_items["product_id"].isin(products["product_id"])
]

order_items = order_items[
    order_items["quantity"] > 0
]

# -------------------------
# Save Cleaned Files
# -------------------------

customers.to_csv(
    f"{CLEAN_PATH}/customers_clean.csv",
    index=False
)

products.to_csv(
    f"{CLEAN_PATH}/products_clean.csv",
    index=False
)

orders.to_csv(
    f"{CLEAN_PATH}/orders_clean.csv",
    index=False
)

order_items.to_csv(
    f"{CLEAN_PATH}/order_items_clean.csv",
    index=False
)

print("Cleaning completed successfully.\n")

print("Customers :", len(customers))
print("Products  :", len(products))
print("Orders    :", len(orders))
print("Items     :", len(order_items))