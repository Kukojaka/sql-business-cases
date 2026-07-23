# SQL Business Cases

A collection of real-world SQL scenarios inspired by everyday tasks of a Data Analyst.

## About

This repository simulates analytical requests from a fictional e-commerce company **TechMart**.

Each case starts with a business question and demonstrates how SQL can be used to transform transactional data into actionable insights.

The project covers:

* SQL fundamentals
* Aggregations
* JOINs
* Common Table Expressions (CTEs)
* Product Analytics
* Customer Analytics
* Revenue Analysis

## Repository Structure

```text
sql-business-cases/

├── database/
│   └── store.db

├── datasets/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   └── order_items.csv

├── scripts/
│   ├── generate_data.py
│   ├── load_to_sqlite.py
│   └── run_query.py

├── solutions/
│   ├── 01_top_products_by_revenue.sql
│   ├── 02_repeat_customers.sql
│   └── 03_top_customers_by_revenue.sql

├── schema.sql
└── README.md
```

## Database

The project uses a simplified e-commerce database containing:

* customers
* products
* orders
* order_items

The database represents customer activity, product information, and transactional data.

Each SQL solution includes:

* Business question
* SQL query
* Data analysis logic
* Expected output
* Business interpretation

# Completed Cases

## SQL Cases

The repository contains SQL solutions for common e-commerce analytics tasks.

1. **Top Products by Revenue**

Business task:
Find the top 10 products generating the highest revenue.

Analysis:
Calculate revenue using product price and quantity sold, then rank products by total revenue.

Solution:
`solutions/01_top_products_by_revenue.sql`


2. **Repeat Customers Analysis**

Business task:
Identify customers who made more than one purchase.

Analysis:
Count orders per customer and analyze customer purchasing behavior.

Solution:
`solutions/02_repeat_customers.sql`


3. **Top Customers by Revenue**

Business task:
Find the customers generating the highest revenue.

Analysis:
Calculate total customer revenue based on purchased products and rank customers by sales value.

Solution:
`solutions/03_top_customers_by_revenue.sql`


4. **Weekly Revenue Trend**

Business task:
Analyze how company revenue changes week by week.

Analysis:
Aggregate sales revenue by week to identify revenue dynamics over time.

Solution:
`solutions/04_weekly_revenue_trend.sql`

5. **Monthly Average Order Value**

Business task:

Analyze how the average order value changes by month.

Analysis:

Calculate revenue for each order, aggregate it by month, and measure the average revenue generated per order.

Solution:

`solutions/05_monthly_average_order_value.sql`

---

6. **Monthly Revenue Growth**

Business task:

Analyze how revenue changes compared to the previous month.

Analysis:

Calculate monthly revenue and compare it with the previous month's revenue using the `LAG()` window function to measure month-over-month growth.

Solution:

`solutions/06_monthly_revenue_growth.sql`

7. **Monthly Customer Ranking**

Business task:

Identify the top revenue-generating customer for each month.

Analysis:

Calculate monthly revenue for every customer and rank customers within each month using the `RANK()` window function.

Solution:

`solutions/07_monthly_customer_ranking.sql`

---

8. **Running Revenue**

Business task:

Analyze cumulative revenue growth throughout the year.

Analysis:

Calculate monthly revenue and use the `SUM() OVER()` window function to compute cumulative revenue from the beginning of the year.

Solution:

`solutions/08_running_revenue.sql`