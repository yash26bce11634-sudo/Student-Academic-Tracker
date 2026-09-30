from storage import load_students, save_students
from validators import get_non_empty, get_mark, find_student

def enter_marks():
    students = load_students()
    student_id = input("Enter student ID: ").strip()
    student = find_student(students, student_id)
    if student is None:
        print("Student not found. Add the student first.")
        return
    subject = get_non_empty("Enter subject name: ").lower()
    mark = get_mark("Enter marks out of 100: ")
    student["marks"][subject] = mark
    save_students(students)
    print("Marks saved successfully.")
