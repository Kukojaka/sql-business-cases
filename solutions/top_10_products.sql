WITH order_items_quant AS (
    SELECT 
        product_id,
        SUM(quantity) AS quant
    FROM order_items
    GROUP BY product_id
)

SELECT 
    p.product_name,
    oiq.quant * p.price AS revenue
FROM order_items_quant oiq
JOIN products p
    USING(product_id)
ORDER BY revenue DESC
LIMIT 10;