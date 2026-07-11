-- Revenue by Customer

SELECT
    c.customer_id,
    c.customer_name,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100)),2) AS total_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.customer_id,c.customer_name
ORDER BY total_revenue DESC;


-- Revenue by Category

SELECT
    p.category,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100)),2) AS revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY revenue DESC;


-- Monthly Revenue

SELECT
    strftime('%Y-%m',o.order_date) AS month,
    ROUND(SUM(oi.quantity*oi.unit_price*(1-oi.discount_percent/100)),2) AS revenue
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY month
ORDER BY month;


-- Top Products

SELECT
    p.product_name,
    SUM(oi.quantity) AS quantity_sold,
    ROUND(SUM(oi.quantity*oi.unit_price),2) AS revenue
FROM products p
JOIN order_items oi
ON p.product_id=oi.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;