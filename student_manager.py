from storage import load_students, save_students
from validators import get_non_empty, find_student

def add_student():
    students = load_students()
    student_id = get_non_empty("Enter student ID: ")
    if find_student(students, student_id):
        print("That ID already exists.")
        return
    name = get_non_empty("Enter student name: ")
    course = get_non_empty("Enter course/section: ")
    students.append({"id": student_id, "name": name, "course": course, "marks": {}})
    save_students(students)
    print("Student added successfully.")

def view_students():
    students = load_students()
    if not students:
        print("No student records found.")
        return
    print("\nID | Name | Course")
    for student in students:
        print(f'{student["id"]} | {student["name"]} | {student["course"]}')

def update_student():
    students = load_students()
    student_id = input("Enter ID to update: ").strip()
    student = find_student(students, student_id)
    if student is None:
        print("Student not found.")
        return
    name = input(f'New name (Enter to keep {student["name"]}): ').strip()
    course = input(f'New course (Enter to keep {student["course"]}): ').strip()
    if name:
        student["name"] = name
    if course:
        student["course"] = course
    save_students(students)
    print("Student updated.")

def delete_student():
    students = load_students()
    student_id = input("Enter ID to delete: ").strip()
    student = find_student(students, student_id)
    if student is None:
        print("Student not found.")
        return
    students.remove(student)
    save_students(students)
    print("Student deleted.")
