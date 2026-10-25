-- 1
SELECT name FROM customers WHERE city = 'Hyderabad' ORDER BY name;

-- 2
SELECT c.customer_id, c.name, COUNT(o.order_id) AS order_count,
       COALESCE(SUM(o.amount), 0) AS total_spend
FROM customers c LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name;

-- 3
SELECT * FROM orders WHERE amount BETWEEN 500 AND 2000;

-- 4
SELECT c.customer_id, c.name, SUM(o.amount) AS total_spend
FROM customers c JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(o.amount) > 1000;

-- 5
WITH totals AS (
  SELECT customer_id, SUM(amount) AS total_spend
  FROM orders GROUP BY customer_id
)
SELECT customer_id, total_spend,
       DENSE_RANK() OVER (ORDER BY total_spend DESC) AS spend_rank
FROM totals;

-- 7
SELECT c.customer_id, c.name
FROM customers c LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL;
