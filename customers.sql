CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    phone VARCHAR(15) NOT NULL,
    city VARCHAR(100) NOT NULL,
    age INTEGER CHECK (age >= 18),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customers (name, email, phone, city, age)
VALUES
('Rahul Sharma', 'rahul@example.com', '9876543210', 'Delhi', 25),
('Priya Singh', 'priya@example.com', '9876543211', 'Mumbai', 28),
('Amit Kumar', 'amit@example.com', '9876543212', 'Chandigarh', 32),
('Neha Verma', 'neha@example.com', '9876543213', 'Delhi', 22),
('Arjun Mehta', 'arjun@example.com', '9876543214', 'Bangalore', 30);

SELECT * FROM customers;

drop table customers

--Create
INSERT INTO customers (name, email, phone, city, age)
VALUES ('Karan Gupta', 'karan@example.com', '9876543215', 'Pune', 27);

--retrive all
SELECT * FROM customers;

--retrive using customer_id
SELECT * FROM customers WHERE customer_id = 1;

--retrive customers belonging to a city
SELECT * FROM customers WHERE city = 'Delhi';

--update
UPDATE customers SET name = 'Rahul Kumar', phone = '9999999999', city = 'Noida'
WHERE customer_id = 6;

--delete
DELETE FROM customers WHERE customer_id = 6;