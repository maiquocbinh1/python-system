
CREATE DATABASE IF NOT EXISTS `pythonsystem`;
USE `pythonsystem`;

-- admin
CREATE TABLE `admin` (
  `Account` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  PRIMARY KEY (`Account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `admin` (`Account`, `Password`) VALUES
('admin', '123456');

-- class
CREATE TABLE `class` (
  `Class` varchar(45) NOT NULL,
  `Name` varchar(45) NOT NULL,
  PRIMARY KEY (`Class`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `class` (`Class`, `Name`) VALUES
('D22DCCN1', 'Công Nghệ Phần Mềm'),
('D22DCCN2', 'Điện Tử Viễn Thông'),
('D22DCCN3', 'Quản trị An ninh Mạng');

-- student
CREATE TABLE `student` (
  `Student_id` int(11) NOT NULL,
  `Dep` varchar(45),
  `course` varchar(45),
  `Year` varchar(45),
  `Semester` varchar(45),
  `Name` varchar(45),
  `Class` varchar(45) NOT NULL,
  `Roll` varchar(45),
  `Gender` varchar(45),
  `Dob` varchar(45),
  `Email` varchar(45),
  `Phone` varchar(45),
  `Address` varchar(45),
  PRIMARY KEY (`Student_id`),
  FOREIGN KEY (`Class`) REFERENCES `class` (`Class`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- subject
CREATE TABLE `subject` (
  `Subject_id` int(11) NOT NULL,
  `Subject_name` varchar(45) NOT NULL,
  `Class` varchar(45) NOT NULL,
  PRIMARY KEY (`Subject_id`),
  FOREIGN KEY (`Class`) REFERENCES `class` (`Class`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- teacher
CREATE TABLE `teacher` (
  `Teacher_id` int(11) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Phone` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `SecurityQ` varchar(45) NOT NULL,
  `SecurityA` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  PRIMARY KEY (`Teacher_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `teacher` (`Teacher_id`, `Name`, `Phone`, `Email`, `SecurityQ`, `SecurityA`, `Password`) VALUES
(1, 'Tran Van A', '6958592698', 'vantran@epu.edu.com', 'Sở thích của bạn', 'Code', '123456');

-- lesson
CREATE TABLE `lesson` (
  `Lesson_id` int(11) NOT NULL,
  `Time_start` time,
  `Time_end` time,
  `Date` varchar(45) NOT NULL,
  `Teacher_id` int(11) NOT NULL,
  `Subject_id` int(11) NOT NULL,
  PRIMARY KEY (`Lesson_id`),
  FOREIGN KEY (`Teacher_id`) REFERENCES `teacher` (`Teacher_id`),
  FOREIGN KEY (`Subject_id`) REFERENCES `subject` (`Subject_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- attendance
CREATE TABLE `attendance` (
  `IdAuttendance` varchar(45) NOT NULL,
  `Student_id` int(11),
  `Name` varchar(45),
  `Class` varchar(45),
  `Time_in` time,
  `Time_out` time,
  `Date` varchar(45),
  `Lesson_id` int(11),
  `AttendanceStatus` varchar(45),
  PRIMARY KEY (`IdAuttendance`),
  FOREIGN KEY (`Student_id`) REFERENCES `student` (`Student_id`) ON DELETE CASCADE,
  FOREIGN KEY (`Lesson_id`) REFERENCES `lesson` (`Lesson_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- student relationship
CREATE TABLE `student_has_subject` (
  `Student_id` int(11) NOT NULL,
  `Subject_id` int(11) NOT NULL,
  FOREIGN KEY (`Student_id`) REFERENCES `student` (`Student_id`) ON DELETE CASCADE,
  FOREIGN KEY (`Subject_id`) REFERENCES `subject` (`Subject_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- teacher relationship
CREATE TABLE `teacher_has_subject` (
  `Teacher_id` int(11) NOT NULL,
  `Subject_id` int(11) NOT NULL,
  FOREIGN KEY (`Teacher_id`) REFERENCES `teacher` (`Teacher_id`) ON DELETE CASCADE,
  FOREIGN KEY (`Subject_id`) REFERENCES `subject` (`Subject_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
