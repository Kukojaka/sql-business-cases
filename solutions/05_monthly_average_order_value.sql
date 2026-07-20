WITH base AS (
    SELECT
        o.order_id,
        strftime('%Y-%m', o.order_date) AS month,
        SUM(oi.quantity * p.price) AS order_revenue
    FROM orders o
    INNER JOIN order_items oi
        USING(order_id)
    INNER JOIN products p
        USING(product_id)
    GROUP BY
        o.order_id,
        month
)

SELECT
    month,
    COUNT(order_id) AS orders,
    SUM(order_revenue) AS revenue,
    ROUND(
        SUM(order_revenue) * 1.0 / COUNT(order_id),
        2
    ) AS average_order_value
FROM base
GROUP BY month
ORDER BY month;