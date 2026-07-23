WITH base AS (
    SELECT
        strftime('%Y-%m', order_date) AS month,
        SUM(price * quantity) AS revenue
    FROM orders
    INNER JOIN order_items USING(order_id)
    INNER JOIN products USING(product_id)
    GROUP BY month
)

SELECT
    month,
    revenue,
    SUM(revenue) OVER (
        ORDER BY month
    ) AS cumulative_revenue
FROM base;