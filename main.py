from student_manager import add_student, view_students, update_student, delete_student
from marks_manager import enter_marks
from reports import student_report, class_report

def show_menu():
    print("\n===== STUDENT ACADEMIC TRACKER =====")
    print("1. Add student")
    print("2. View students")
    print("3. Update student")
    print("4. Delete student")
    print("5. Enter marks")
    print("6. Student report")
    print("7. Class report")
    print("8. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            enter_marks()
        elif choice == "6":
            student_report()
        elif choice == "7":
            class_report()
        elif choice == "8":
            print("Thank you for using the tracker!")
            break
        else:
            print("Invalid choice. Please enter 1 to 8.")

if __name__ == "__main__":
    main()
