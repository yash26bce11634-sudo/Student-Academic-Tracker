from storage import load_students
from validators import find_student

def calculate_percentage(marks):
    if not marks:
        return None
    return sum(marks.values()) / len(marks)

def student_report():
    students = load_students()
    student_id = input("Enter student ID: ").strip()
    student = find_student(students, student_id)
    if student is None:
        print("Student not found.")
        return
    print(f'\nReport for {student["name"]} ({student["id"]})')
    print("Course:", student["course"])
    if not student["marks"]:
        print("No marks entered yet.")
        return
    for subject, mark in student["marks"].items():
        print(f"{subject.title()}: {mark:g}/100")
    percentage = calculate_percentage(student["marks"])
    print(f"Average: {percentage:.2f}%")
    print("Status:", "Pass" if percentage >= 40 else "Needs improvement")

def class_report():
    students = load_students()
    if not students:
        print("No student records found.")
        return
    print("\n===== CLASS SUMMARY =====")
    print("Total students:", len(students))
    with_marks = 0
    class_averages = []
    for student in students:
        average = calculate_percentage(student["marks"])
        if average is not None:
            with_marks += 1
            class_averages.append(average)
            print(f'{student["name"]}: {average:.2f}%')
        else:
            print(f'{student["name"]}: marks not entered')
    print("Students with marks:", with_marks)
    if class_averages:
        print(f"Class average: {sum(class_averages) / len(class_averages):.2f}%")
