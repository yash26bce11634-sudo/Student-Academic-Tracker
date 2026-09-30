def get_non_empty(prompt):
    """Keep asking until the user enters non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")

def get_mark(prompt):
    """Get a mark between 0 and 100."""
    while True:
        try:
            mark = float(input(prompt))
            if 0 <= mark <= 100:
                return mark
            print("Mark must be between 0 and 100.")
        except ValueError:
            print("Please enter a number.")

def find_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None
