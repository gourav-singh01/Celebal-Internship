import argparse
import sqlite3
from tabulate import tabulate
import pandas as pd

conn = sqlite3.connect("database/ecommerce.db")

reports = {

    "revenue": "SELECT customer_name, ROUND(SUM(quantity*unit_price),2) AS revenue FROM customers c JOIN orders o ON c.customer_id=o.customer_id JOIN order_items oi ON o.order_id=oi.order_id GROUP BY customer_name ORDER BY revenue DESC LIMIT 10",

    "products": "SELECT product_name, SUM(quantity) AS quantity FROM products p JOIN order_items oi ON p.product_id=oi.product_id GROUP BY product_name ORDER BY quantity DESC LIMIT 10",

    "customers": "SELECT customer_name, customer_type FROM customers LIMIT 20",

    "segments": """
    SELECT
        c.customer_name,
        COUNT(DISTINCT o.order_id) AS total_orders,
        ROUND(SUM(oi.quantity * oi.unit_price),2) AS total_spent,
        CASE
            WHEN COUNT(DISTINCT o.order_id) = 1 THEN 'One-Time'
            WHEN COUNT(DISTINCT o.order_id) BETWEEN 2 AND 5 THEN 'Occasional'
            ELSE 'Loyal'
        END AS customer_segment
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    GROUP BY c.customer_id, c.customer_name
    ORDER BY total_spent DESC
    LIMIT 20
    """

}

parser=argparse.ArgumentParser()

parser.add_argument("--report",required=True)

args=parser.parse_args()

if args.report not in reports:
    print("Available Reports : revenue | products | customers")
else:
    df=pd.read_sql_query(reports[args.report],conn)

    if df.empty:
        print("No data found.")
    else:
        print(tabulate(df,headers="keys",tablefmt="grid",showindex=False))

conn.close()