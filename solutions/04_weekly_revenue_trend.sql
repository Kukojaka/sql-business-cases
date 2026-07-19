WITH base AS (
    SELECT 
        order_date,
        order_id,
        SUM(oi.quantity * p.price) AS revenue
    FROM orders
    INNER JOIN order_items oi USING(order_id)
    INNER JOIN products p USING(product_id)
    GROUP BY order_date, order_id
)

SELECT
    strftime('%Y-%W', order_date) AS week,
    SUM(revenue) AS revenue
FROM base
GROUP BY week
ORDER BY week;