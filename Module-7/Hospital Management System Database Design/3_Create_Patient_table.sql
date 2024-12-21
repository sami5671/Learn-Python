CREATE TABLE `patients` (
    `patientID` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `age` INT NOT NULL,
    `gender` VARCHAR(10) NOT NULL,
    `phone` VARCHAR(20) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
)