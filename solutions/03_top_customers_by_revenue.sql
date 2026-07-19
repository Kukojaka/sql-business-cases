SELECT 
full_name,
SUM(price*quantity) AS revenue
FROM orders
INNER JOIN order_items using(order_id)
INNER JOIN products using(product_id)
INNER JOIN customers using(customer_id)
GROUP BY customer_id, full_name
ORDER BY revenue DESC
LIMIT 10;