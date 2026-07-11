WITH customer_sales AS
(
SELECT
c.customer_id,
c.customer_name,
SUM(oi.quantity*oi.unit_price) AS lifetime_value
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY c.customer_id,c.customer_name
)

SELECT
*,
RANK() OVER(ORDER BY lifetime_value DESC) AS customer_rank,
DENSE_RANK() OVER(ORDER BY lifetime_value DESC) AS dense_rank
FROM customer_sales;
-- Running Revenue

SELECT
    strftime('%Y-%m',o.order_date) AS month,

    ROUND(
        SUM(oi.quantity*oi.unit_price),
        2
    ) AS monthly_revenue,

    ROUND(
        SUM(
            SUM(oi.quantity*oi.unit_price)
        ) OVER(
            ORDER BY strftime('%Y-%m',o.order_date)
        ),
        2
    ) AS running_total

FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id

GROUP BY month;