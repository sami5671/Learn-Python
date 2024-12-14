-- Step 1: Create the table
CREATE TABLE customers (
    AccountID INT PRIMARY KEY,           -- Unique account identifier
    CustomerName VARCHAR(100),           -- Customer's full name
    AccountNumber VARCHAR(20),           -- Bank account number
    AccountType VARCHAR(50),             -- Type of account (e.g., Savings, Checking)
    Balance DECIMAL(15, 2),              -- Account balance
    BranchName VARCHAR(100),             -- Bank branch name
    Email VARCHAR(100),                  -- Customer's email address
    PhoneNumber VARCHAR(15)              -- Customer's phone number
);

-- Step 2: Insert 15 rows of data
INSERT INTO customers (AccountID, CustomerName, AccountNumber, AccountType, Balance, BranchName, Email, PhoneNumber)
VALUES
(1, 'John Doe', '123456789012', 'Savings', 1500.50, 'Downtown Branch', 'johndoe@example.com', '123-456-7890'),
(2, 'Jane Smith', '987654321098', 'Checking', 2400.75, 'Uptown Branch', 'janesmith@example.com', '987-654-3210'),
(3, 'Robert Brown', '456789123456', 'Savings', 3200.00, 'Main Street Branch', 'robertbrown@example.com', '456-789-1234'),
(4, 'Emily Davis', '789456123789', 'Checking', 1000.20, 'City Center Branch', 'emilydavis@example.com', '789-456-1230'),
(5, 'Michael Johnson', '321654987321', 'Savings', 5600.80, 'Greenwood Branch', 'michaelj@example.com', '321-654-9876'),
(6, 'Linda White', '654321987654', 'Checking', 250.75, 'Hilltop Branch', 'lindawhite@example.com', '654-321-9876'),
(7, 'David Lee', '159753468213', 'Savings', 4800.60, 'Lakeside Branch', 'davidlee@example.com', '159-753-4682'),
(8, 'Sarah Wilson', '753159846357', 'Checking', 700.00, 'West End Branch', 'sarahwilson@example.com', '753-159-8463'),
(9, 'Chris Hall', '951753486213', 'Savings', 920.10, 'Riverside Branch', 'chrishall@example.com', '951-753-4862'),
(10, 'Anna King', '654789321456', 'Checking', 1300.00, 'Sunset Branch', 'annaking@example.com', '654-789-3214'),
(11, 'James Scott', '123987456123', 'Savings', 1450.30, 'Maplewood Branch', 'jamesscott@example.com', '123-987-4561'),
(12, 'Jessica Green', '987321654987', 'Checking', 750.90, 'Elmwood Branch', 'jessicagreen@example.com', '987-321-6549'),
(13, 'Thomas Adams', '789654321789', 'Savings', 3800.00, 'Oakwood Branch', 'thomasadams@example.com', '789-654-3217'),
(14, 'Karen Mitchell', '321987654321', 'Checking', 1150.75, 'Pinehill Branch', 'karenmitchell@example.com', '321-987-6543'),
(15, 'Daniel Garcia', '654123987654', 'Savings', 2950.25, 'Riverbend Branch', 'danielgarcia@example.com', '654-123-9876');
