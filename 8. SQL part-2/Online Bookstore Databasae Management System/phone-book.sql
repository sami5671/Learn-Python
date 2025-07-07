-- Active: 1734951938100@@127.0.0.1@3306@phone_book
CREATE TABLE contacts (
    contact_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- modify column
ALTER TABLE contacts
    ADD COLUMN address VARCHAR(255) AFTER email;

ALTER TABLE contacts
    ADD COLUMN test_column VARCHAR(40) FIRST;

ALTER TABLE contacts
    ADD COLUMN last_test VARCHAR(40);

ALTER TABLE contacts
    CHANGE COLUMN address customer_address VARCHAR(255);



-- index on last_name
CREATE INDEX idx_last_name ON contacts (last_name);

-- check index
SHOW INDEX FROM contacts;

SELECT * FROM contacts WHERE last_name = 'Taylor';

INSERT INTO contacts (first_name, last_name, phone, email)
VALUES 
('John', 'Doe', '1234567890', 'johndoe@example.com'),
('Jane', 'Smith', '9876543210', 'janesmith@example.com'),
('Robert', 'Johnson', '5551234567', 'robert.johnson@example.com'),
('Emily', 'Davis', '4449876543', 'emily.davis@example.com'),
('Michael', 'Brown', '3336549872', 'michael.brown@example.com'),
('Sarah', 'Taylor', '2229871234', 'sarah.taylor@example.com'),
('David', 'Anderson', '1114567890', 'david.anderson@example.com'),
('Laura', 'Harris', '6669876543', 'laura.harris@example.com'),
('James', 'Martin', '7776541234', 'james.martin@example.com'),
('Sophia', 'Wilson', '8881239876', 'sophia.wilson@example.com');