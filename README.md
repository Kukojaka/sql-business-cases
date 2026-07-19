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

## Case 1: Top Products by Revenue

**Business question:**
Which products generate the highest revenue?

**Tables:**

* products
* order_items

**Metric:**

```text
revenue = price * quantity
```

**Analysis:**

* calculate total quantity sold per product
* multiply by product price
* rank products by revenue

**Solution:**

```text
solutions/01_top_products_by_revenue.sql
```

---

## Case 2: Repeat Customers Analysis

**Business question:**
Which customers make repeat purchases?

**Tables:**

* customers
* orders

**Metrics:**

```text
total_orders = COUNT(order_id)
```

**Analysis:**

* count orders per customer
* identify customers with more than one purchase
* calculate first and latest order dates

**Solution:**

```text
solutions/02_repeat_customers.sql
```

---

## Case 3: Top Customers by Revenue

**Business question:**
Which customers generate the highest revenue?

**Tables:**

* customers
* orders
* order_items
* products

**Metric:**

```text
revenue = price * quantity
```

**Analysis:**

* connect customers with their orders
* calculate revenue from purchased products
* aggregate revenue per customer
* rank customers by total revenue

**Solution:**

```text
solutions/03_top_customers_by_revenue.sql
```
