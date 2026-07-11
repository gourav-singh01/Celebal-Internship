WITH first_purchase AS
(
SELECT
customer_id,
MIN(date(order_date)) AS first_purchase
FROM orders
GROUP BY customer_id
)

SELECT
strftime('%Y-%m',first_purchase) AS cohort,
COUNT(customer_id) AS customers
FROM first_purchase
GROUP BY cohort
ORDER BY cohort;
-- Repeat Customers

SELECT
customer_id,
COUNT(order_id) AS total_orders,

CASE

WHEN COUNT(order_id)=1
THEN 'One-Time'

ELSE 'Repeat'

END AS customer_type

FROM orders

GROUP BY customer_id;