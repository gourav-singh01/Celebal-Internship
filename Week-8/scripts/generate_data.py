import os
import random
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

# -----------------------------
# Create output directory
# -----------------------------
RAW_PATH = "data/raw"
os.makedirs(RAW_PATH, exist_ok=True)

NUM_CUSTOMERS = 500
NUM_PRODUCTS = 500
NUM_ORDERS = 1000
NUM_ORDER_ITEMS = 2500

# -----------------------------
# Customers
# -----------------------------
customers = []

customer_types = ["REGULAR", "PREMIUM", "VIP"]

for i in range(1, NUM_CUSTOMERS + 1):

    email = fake.email()

    # 2% invalid emails
    if random.random() < 0.02:
        email = email.replace("@", "")

    customers.append({
        "customer_id": i,
        "customer_name": fake.name(),
        "email": email,
        "registration_date": fake.date_between(
            start_date="-3y",
            end_date="today"
        ),
        "customer_type": random.choice(customer_types)
    })

customers_df = pd.DataFrame(customers)

# duplicate rows
customers_df = pd.concat(
    [
        customers_df,
        customers_df.sample(10, random_state=42)
    ],
    ignore_index=True
)

# -----------------------------
# Products
# -----------------------------
categories = {
    "Electronics": [
        "Laptop",
        "Phone",
        "Headphones",
        "Camera"
    ],
    "Clothing": [
        "T-Shirt",
        "Jeans",
        "Jacket",
        "Shoes"
    ],
    "Books": [
        "Novel",
        "Biography",
        "Dictionary",
        "Magazine"
    ],
    "Home": [
        "Chair",
        "Table",
        "Lamp",
        "Fan"
    ]
}

products = []

for i in range(1, NUM_PRODUCTS + 1):

    category = random.choice(list(categories.keys()))
    product_name = random.choice(categories[category])

    # dirty names
    if random.random() < 0.05:
        product_name = "   " + product_name.lower() + "   "

    products.append({
        "product_id": i,
        "product_name": product_name,
        "category": category,
        "subcategory": fake.word().title(),
        "cost_price": round(random.uniform(100, 50000), 2)
    })

products_df = pd.DataFrame(products)

products_df = pd.concat(
    [
        products_df,
        products_df.sample(10, random_state=42)
    ],
    ignore_index=True
)

print("Customers Created :", len(customers_df))
print("Products Created  :", len(products_df))
# -----------------------------
# Orders
# -----------------------------
orders = []

order_status = [
    "PLACED",
    "SHIPPED",
    "DELIVERED",
    "CANCELLED",
    "RETURNED"
]

for i in range(1, NUM_ORDERS + 1):

    customer_id = random.randint(1, NUM_CUSTOMERS)

    # Around 5% missing customer ids
    if random.random() < 0.05:
        customer_id = None

    order_date = fake.date_time_between(
        start_date="-2y",
        end_date="now"
    )

    # Few dates in wrong format
    if random.random() < 0.03:
        order_date = order_date.strftime("%d-%m-%Y")
    else:
        order_date = order_date.strftime("%Y-%m-%d %H:%M:%S")

    orders.append({
        "order_id": i,
        "customer_id": customer_id,
        "order_date": order_date,
        "status": random.choice(order_status),
        "region_code": random.choice(
            ["NORTH", "SOUTH", "EAST", "WEST"]
        )
    })

orders_df = pd.DataFrame(orders)

# duplicate rows
orders_df = pd.concat(
    [
        orders_df,
        orders_df.sample(20, random_state=42)
    ],
    ignore_index=True
)

print("Orders Created    :", len(orders_df))


# -----------------------------
# Order Items
# -----------------------------
order_items = []

for i in range(1, NUM_ORDER_ITEMS + 1):

    order_id = random.randint(1, NUM_ORDERS)

    # Few invalid order ids
    if random.random() < 0.02:
        order_id = NUM_ORDERS + random.randint(50, 150)

    quantity = random.randint(1, 5)

    # Negative quantity
    if random.random() < 0.03:
        quantity = -quantity

    order_items.append({
        "item_id": i,
        "order_id": order_id,
        "product_id": random.randint(1, NUM_PRODUCTS),
        "quantity": quantity,
        "unit_price": round(random.uniform(200, 50000), 2),
        "discount_percent": random.randint(0, 40)
    })

order_items_df = pd.DataFrame(order_items)

print("Order Items       :", len(order_items_df))


# -----------------------------
# Save CSV files
# -----------------------------
customers_df.to_csv(
    os.path.join(RAW_PATH, "customers.csv"),
    index=False
)

products_df.to_csv(
    os.path.join(RAW_PATH, "products.csv"),
    index=False
)

orders_df.to_csv(
    os.path.join(RAW_PATH, "orders.csv"),
    index=False
)

order_items_df.to_csv(
    os.path.join(RAW_PATH, "order_items.csv"),
    index=False
)

print("\nRaw datasets generated successfully.")
print("Location :", RAW_PATH)