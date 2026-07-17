# SQL Business Cases

A collection of real-world SQL scenarios inspired by everyday tasks of a Data Analyst.

## About

This repository simulates analytical requests from a fictional e-commerce company **TechMart**. Each case starts with a business question and demonstrates how SQL can be used to extract insights from transactional data.

The repository covers:

* SQL fundamentals
* Aggregations
* JOINs
* Common Table Expressions (CTEs)
* Window Functions
* Cohort Analysis
* Product Analytics
* Customer Analytics
* Revenue Analysis

## Repository Structure

```text
schema.sql
insert_data.sql
solutions/
images/
```

## Database

The project uses a simplified e-commerce database containing customers, products, orders, payments, and categories.

Each SQL solution includes:

* Business context
* SQL query
* Explanation
* Expected output
* Business interpretation

## Case 1: Top 10 Products by Revenue

Business question:
Which products generate the highest revenue?

Tables:
- products
- order_items

Metric:
revenue = price * quantity

Solution:
solutions/top_10_products.sql