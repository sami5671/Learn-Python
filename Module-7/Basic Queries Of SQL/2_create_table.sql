-- Step 1: Create Independent Tables


-- Create table regio
CREATE TABLE regions (
    region_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    region_name VARCHAR(25) DEFAULT NULL
);

-- Create table jobs
CREATE TABLE jobs (
    job_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    job_title VARCHAR(35) NOT NULL,
    min_salary DECIMAL(8, 2) DEFAULT NULL,
    max_salary DECIMAL(8, 2) DEFAULT NULL
);
