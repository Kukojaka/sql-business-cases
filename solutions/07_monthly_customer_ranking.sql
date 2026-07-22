WITH base AS (
    SELECT
        strftime('%Y-%m', order_date) AS month,
        full_name,
        SUM(price * quantity) AS revenue
    FROM orders
    INNER JOIN customers USING(customer_id)
    INNER JOIN order_items USING(order_id)
    INNER JOIN products USING(product_id)
    GROUP BY
        month,
        full_name
),

ranking AS (
    SELECT
        month,
        full_name,
        revenue,
        RANK() OVER(
            PARTITION BY month
            ORDER BY revenue DESC
        ) AS top
    FROM base
)

SELECT
    month,
    full_name,
    revenue
FROM ranking
WHERE top = 1
ORDER BY month;