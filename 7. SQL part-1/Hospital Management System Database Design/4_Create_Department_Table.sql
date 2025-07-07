CREATE TABLE `departments` (
    `departmentID` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `location` VARCHAR(50) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),

    `doctorId` BIGINT UNSIGNED,
    FOREIGN KEY (`doctorId`) REFERENCES `doctors`(`doctorId`)
)