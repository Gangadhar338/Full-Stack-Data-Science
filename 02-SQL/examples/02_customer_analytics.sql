-- Portable SQL example; run after creating the customers and orders tables
-- from lessons/02-core-concepts.md.
SELECT c.customer_id, c.name,
       COUNT(o.order_id) AS order_count,
       COALESCE(SUM(o.amount), 0) AS total_spend
FROM customers AS c
LEFT JOIN orders AS o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spend DESC, c.name;
