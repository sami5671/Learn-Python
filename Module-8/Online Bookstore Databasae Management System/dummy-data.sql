INSERT INTO authors (name, email) VALUES
('J.K. Rowling', 'jkrowling@example.com'),
('George R.R. Martin', 'grrm@example.com'),
('J.R.R. Tolkien', 'jrrtolkien@example.com'),
('Stephen King', 'stephenking@example.com');

INSERT INTO books (title, price, stock_quantity, author_id) VALUES
('Harry Potter and the Philosopher\'s Stone', 39.99, 50, 1),
('A Game of Thrones', 49.99, 30, 2),
('The Lord of the Rings', 59.99, 20, 3),
('The Shining', 29.99, 40, 4);

INSERT INTO customers (name, email, phone) VALUES
('Alice Johnson', 'alice.johnson@example.com', '123-456-7890'),
('Bob Smith', 'bob.smith@example.com', '987-654-3210'),
('Charlie Brown', 'charlie.brown@example.com', '555-666-7777');


INSERT INTO orders (customer_id, order_date, total_amount) VALUES
(1, '2024-12-20 14:30:00', 69.98),
(2, '2024-12-21 16:00:00', 49.99),
(3, '2024-12-22 11:15:00', 29.99);

INSERT INTO order_details (order_id, book_id, quantity, line_total) VALUES
(1, 1, 1, 39.99), -- Alice bought 1 copy of "Harry Potter"
(1, 4, 1, 29.99), -- Alice also bought 1 copy of "The Shining"
(2, 2, 1, 49.99), -- Bob bought 1 copy of "A Game of Thrones"
(3, 4, 1, 29.99); -- Charlie bought 1 copy of "The Shining"