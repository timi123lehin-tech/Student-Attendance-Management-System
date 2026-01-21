# Student Attendance Management System

attendance_records = {}

def mark_attendance(student_name, status):
    attendance_records[student_name] = status

def display_attendance(attendance_records):
    print("\nStudent Attendance Record")
    print("-------------------------")
    for student, status in attendance_records.items():
        print(f"{student}: {status}")

# Main program
mark_attendance("Timi", "Present")
mark_attendance("Faith", "Absent")
mark_attendance("John", "Present")
mark_attendance("Mary", "Present")

display_attendance(attendance_records)
