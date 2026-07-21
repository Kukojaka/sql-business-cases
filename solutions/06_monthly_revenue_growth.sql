WITH previous AS (
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
    LAG(revenue) OVER(ORDER BY month) AS previous_revenue,
    ROUND(
        (revenue - LAG(revenue) OVER(ORDER BY month)) * 100.0
        / LAG(revenue) OVER(ORDER BY month),
        2
    ) AS growth_pct
FROM previous
ORDER BY month;