NAME: Obembe OluwaTimilehin Daniel
Matric Number: 25/17821

-- Student Attendance Management System

-- Course
SEN 201 – Software Engineering

-- Project Description
The Student Attendance Management System is a simple Python-based software application developed to record and display the attendance status of students in a class. The system helps lecturers or administrators keep track of students who are present or absent during a class session.

---

-- Software Development Life Cycle (SDLC)

This project was developed using the Software Development Life Cycle (SDLC) methodology, which provides a structured approach to software development. The stages used in this project are explained below.

---

-- 1. Planning
The planning stage defines the purpose and objectives of the system.

--- Objectives:
- To develop a system that records student attendance.
- To display attendance records in a clear and organized manner.

--- Tools Used:
- Programming Language: Python
- Code Editor: Visual Studio Code
- Version Control System: Git
- Repository Hosting Platform: GitHub

---

-- 2. Requirement Analysis
This stage identifies what the system is expected to do.

--- Functional Requirements:
- The system should store student names.
- The system should allow students to be marked as Present or Absent.
- The system should display attendance records.

--- Non-Functional Requirements:
- The system should be simple and easy to use.
- The system should provide accurate attendance information.

---

-- 3. System Design
This stage defines how the system will operate internally.

--- Data Structure:
- A dictionary is used to store student names and their attendance status.

--- Functions Designed:
- mark_attendance(student_name, status)
- display_attendance(attendance_records)

The names of variables and functions used in the design are the same as those used in the implementation to maintain consistency.

---

-- 4. Implementation
The system was implemented using Python programming language.

--- Source Code (attendance.py):

```python
- Student Attendance Management System

attendance_records = {}

def mark_attendance(student_name, status):
    attendance_records[student_name] = status

def display_attendance(attendance_records):
    print("\nStudent Attendance Record")
    print("-------------------------")
    for student, status in attendance_records.items():
        print(f"{student}: {status}")

- Main program
mark_attendance("Timi", "Present")
mark_attendance("Faith", "Absent")
mark_attendance("John", "Present")
mark_attendance("Mary", "Present")

display_attendance(attendance_records)
```

-- 5. Testing
The system was tested using different student names and attendance statuses to ensure that attendance records were displayed correctly without errors.

-- 6. Deployment
After successful testing, the project was deployed by pushing the source code to a GitHub repository using Git for version control.

-- Conclusion
The Student Attendance Management System was successfully developed by following all stages of the Software Development Life Cycle. The project meets its objectives and demonstrates the application of SDLC principles in software development.


-- AUTHOR: TIMILEHIN.

