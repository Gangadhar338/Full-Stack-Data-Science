CREATE TABLE customers (id INTEGER PRIMARY KEY, name VARCHAR(100));
CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, amount DECIMAL(10,2));
SELECT c.id,c.name,SUM(o.amount) revenue FROM customers c JOIN orders o ON o.customer_id=c.id GROUP BY c.id,c.name ORDER BY revenue DESC;
SELECT c.id,c.name FROM customers c LEFT JOIN orders o ON o.customer_id=c.id WHERE o.id IS NULL;
