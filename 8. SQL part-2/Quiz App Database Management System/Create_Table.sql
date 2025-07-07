-- Active: 1734610841060@@127.0.0.1@3306@quiz_app_management_system

--------Create Users Table--------
CREATE Table `users`(
    `userId` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `role` VARCHAR(100) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
)

--------Create Quizzes Table--------
CREATE TABLE `quizzes` (
    `quizID` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(100) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),

    `teacher_id` BIGINT UNSIGNED,
    FOREIGN KEY (`teacher_id`) REFERENCES `users`(`userId`)
)

--------Create Questions Table--------
CREATE TABLE `questions` (
    `questionID` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `text` VARCHAR(1000) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),

    `quiz_id` BIGINT UNSIGNED,
    FOREIGN KEY (`quiz_id`) REFERENCES `quizzes`(`quizID`)
)

--------Create Options Table--------
CREATE TABLE `options` (
    `optionID` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `text` VARCHAR(1000) NOT NULL,
    `is_correct` BOOLEAN NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),

    `question_id` BIGINT UNSIGNED,
    FOREIGN KEY (`question_id`) REFERENCES `questions`(`questionID`)
)

--------Create Student_Answers Table--------
CREATE TABLE `student_answers` (
    `studentAnswersID` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,

    `student_id` BIGINT UNSIGNED,
    FOREIGN KEY (`student_id`) REFERENCES `users`(`userId`),

    `quiz_id` BIGINT UNSIGNED,
    FOREIGN KEY (`quiz_id`) REFERENCES `quizzes`(`quizID`),

    `question_id` BIGINT UNSIGNED,
    FOREIGN KEY (`question_id`) REFERENCES `questions`(`questionID`),

    `option_id` BIGINT UNSIGNED,
    FOREIGN KEY (`option_id`) REFERENCES `options`(`optionID`),

    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
)
