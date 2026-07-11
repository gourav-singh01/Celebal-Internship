SELECT
    c.customer_id,
    c.customer_name,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(SUM(oi.quantity * oi.unit_price),2) AS total_spent,

    CASE
        WHEN COUNT(DISTINCT o.order_id) = 1 THEN 'One-Time'
        WHEN COUNT(DISTINCT o.order_id) BETWEEN 2 AND 5 THEN 'Occasional'
        ELSE 'Loyal'
    END AS customer_segment

FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_items oi
ON o.order_id = oi.order_id

GROUP BY c.customer_id,c.customer_name
ORDER BY total_spent DESC;