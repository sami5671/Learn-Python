--------Create database--------
CREATE DATABASE hospital_management_system

--------Create Doctor Table--------
CREATE Table `doctors`(
    `doctorId` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `specialization` VARCHAR(100) NOT NULL,
    `phone` VARCHAR(20) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
)

--------Create Patient Table--------
CREATE TABLE `patients` (
    `patientID` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `age` INT NOT NULL,
    `gender` VARCHAR(10) NOT NULL,
    `phone` VARCHAR(20) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
)


--------Create Department Table--------
CREATE TABLE `departments` (
    `departmentID` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `location` VARCHAR(50) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),

    `doctorId` BIGINT UNSIGNED,
    FOREIGN KEY (`doctorId`) REFERENCES `doctors`(`doctorId`)
)


--------Create Appointments Table--------
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