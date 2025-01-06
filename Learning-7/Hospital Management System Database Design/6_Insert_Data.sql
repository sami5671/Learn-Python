INSERT INTO `doctors` (`name`, `specialization`, `phone`) 
VALUES
    ("Mr. Ostad", "Cardiology", "0134141343"),
    ("Dr. Ayesha", "Neurology", "01712345678"),
    ("Dr. Kabir", "Orthopedics", "01698765432"),
    ("Dr. Rahim", "Pediatrics", "01811223344"),
    ("Dr. Laila", "Dermatology", "01999887766");


INSERT INTO `patients` (`name`, `age`, `gender`, `phone`) 
VALUES
    ("Mr. Hasan", 45, "Male", "01312345678"),
    ("Ms. Sumi", 30, "Female", "01498765432"),
    ("Mr. Rafique", 60, "Male", "01511223344"),
    ("Ms. Mita", 25, "Female", "01699887766"),
    ("Mr. Jamal", 50, "Male", "01744556677");

INSERT INTO `departments` (`name`, `location`, `doctorId`) 
VALUES
    ("Cardiology", "Dhaka", 1),
    ("Neurology", "Chittagong", 2),
    ("Orthopedics", "Khulna", 3),
    ("Pediatrics", "Rajshahi", 4),
    ("Dermatology", "Sylhet", 5);

INSERT INTO `appointments` (`date`, `time`, `status`, `doctorId`, `patientID`) 
VALUES
    ("2024-12-22", "10:00:00", "Scheduled", 1, 1),
    ("2024-12-23", "11:30:00", "Completed", 2, 2),
    ("2024-12-24", "09:45:00", "Cancelled", 3, 3),
    ("2024-12-25", "14:00:00", "Scheduled", 4, 4),
    ("2024-12-26", "16:15:00", "Rescheduled", 5, 5);
