CREATE TABLE `appointments` (
    `appointmentID` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `date` DATE,
    `time` TIME,
    `status` VARCHAR(20) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),

    `doctorId` BIGINT UNSIGNED,
    `patientID` BIGINT UNSIGNED,
    FOREIGN KEY (`doctorId`) REFERENCES `doctors`(`doctorId`),
    FOREIGN KEY (`patientID`) REFERENCES `patients`(`patientID`)
)