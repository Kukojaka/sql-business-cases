SELECT 
    customer_id,
    COUNT(order_id) AS order_quantity,
    first_value(order_date) over (order by order_date),
    last_value(order_date) over (order by order_date)
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 1;