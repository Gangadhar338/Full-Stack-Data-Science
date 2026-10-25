# SQL Core Concepts — From Beginner to Practical

## 1. What SQL is
SQL (Structured Query Language) is used to define, read, change, and manage relational data. A table has columns (fields) and rows (records). A primary key uniquely identifies a row; a foreign key links rows between tables.

## 2. Create sample tables
```sql
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL CHECK (amount >= 0),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

## 3. Read, filter, and sort
```sql
SELECT name, city
FROM customers
WHERE city = 'Hyderabad'
ORDER BY name;
```
`SELECT` chooses columns, `FROM` chooses a table, `WHERE` filters rows, and `ORDER BY` sorts results. Use `IS NULL` rather than `= NULL`.

## 4. Aggregation and grouping
```sql
SELECT customer_id, COUNT(*) AS order_count, SUM(amount) AS total_spend
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 1000;
```
`WHERE` filters rows before grouping; `HAVING` filters grouped results.

## 5. Joins
```sql
SELECT c.name, o.order_id, o.amount
FROM customers AS c
JOIN orders AS o ON o.customer_id = c.customer_id;
```
`INNER JOIN` returns matching rows; `LEFT JOIN` keeps all left-side rows even when there is no match.

## 6. CTEs and window functions
```sql
WITH customer_totals AS (
    SELECT customer_id, SUM(amount) AS spend
    FROM orders
    GROUP BY customer_id
)
SELECT customer_id, spend,
       DENSE_RANK() OVER (ORDER BY spend DESC) AS spend_rank
FROM customer_totals;
```
A CTE (`WITH`) names a query for readability. Window functions calculate across related rows without collapsing them like `GROUP BY`.

## 7. Transactions and indexes
Use `BEGIN`, `COMMIT`, and `ROLLBACK` to group related changes safely. Index columns used frequently for joins or filters, but remember indexes consume storage and can slow writes. Confirm plans with your database's `EXPLAIN`.

## Common mistakes
- Joining tables on the wrong key, creating duplicate rows.
- Using `WHERE` for aggregate conditions instead of `HAVING`.
- Forgetting that NULL represents missing/unknown data.
- Using `SELECT *` in production queries when only a few columns are needed.

## Practice checklist
1. Return all customers from one city.
2. Find each customer's total spend.
3. Find customers with no orders using `LEFT JOIN`.
4. Rank customers by spend.
5. Explain when a transaction should be rolled back.
