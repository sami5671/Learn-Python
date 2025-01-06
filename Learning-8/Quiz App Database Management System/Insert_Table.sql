-- Insert data into users table
INSERT INTO `users` (`name`, `role`) VALUES
('Alice Smith', 'Teacher'),
('Bob Johnson', 'Student'),
('Charlie Brown', 'Teacher'),
('Diana Prince', 'Student'),
('Eve Adams', 'Student'),
('Frank Castle', 'Teacher'),
('Grace Hopper', 'Student'),
('Henry Ford', 'Student'),
('Isla Fisher', 'Teacher'),
('Jack Sparrow', 'Student');

-- Insert data into quizzes table
INSERT INTO `quizzes` (`title`, `teacher_id`) VALUES
('Math Quiz 1', 1),
('Science Quiz 1', 3),
('History Quiz 1', 1),
('Math Quiz 2', 6),
('Geography Quiz 1', 9),
('Science Quiz 2', 6),
('History Quiz 2', 9),
('Math Quiz 3', 3),
('Physics Quiz 1', 9),
('Biology Quiz 1', 1);

-- Insert data into questions table
INSERT INTO `questions` (`text`, `quiz_id`) VALUES
('What is 2 + 2?', 1),
('What is the boiling point of water?', 2),
('Who discovered America?', 3),
('What is the square root of 16?', 1),
('What is the capital of France?', 5),
('What is Newton\'s third law?', 6),
('When was the American Civil War?', 3),
('What is 3 x 3?', 4),
('Define acceleration.', 6),
('What is the function of mitochondria?', 10);

-- Insert data into options table
INSERT INTO `options` (`text`, `is_correct`, `question_id`) VALUES
('4', TRUE, 1),
('5', FALSE, 1),
('100°C', TRUE, 2),
('90°C', FALSE, 2),
('Christopher Columbus', TRUE, 3),
('Albert Einstein', FALSE, 3),
('4', TRUE, 4),
('8', FALSE, 4),
('Paris', TRUE, 5),
('Berlin', FALSE, 5),
('Equal and opposite reaction', TRUE, 6),
('Action only', FALSE, 6),
('1861-1865', TRUE, 7),
('1800-1850', FALSE, 7),
('9', TRUE, 8),
('12', FALSE, 8),
('Rate of change of velocity', TRUE, 9),
('Force per unit area', FALSE, 9),
('Powerhouse of the cell', TRUE, 10),
('Brain of the cell', FALSE, 10);

-- Insert data into student_answers table
INSERT INTO `student_answers` (`student_id`, `quiz_id`, `question_id`, `option_id`) VALUES
(2, 1, 1, 1),
(4, 1, 1, 1),
(5, 2, 2, 3),
(8, 3, 3, 5),
(2, 4, 4, 7),
(4, 5, 5, 9),
(5, 6, 6, 11),
(8, 7, 7, 13),
(2, 8, 8, 15),
(4, 10, 10, 19);
