class Test:
    def __init__(self, grade):
        self.grade = grade

class Subject(Test):
    def __init__(self, name, grade):
        super().__init__(grade)
        self.name = name

class Student(Subject):
    def __init__(self, name):
        self.name = name
        self.subjects = []

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def main():
    subjects = {
        1: "history",
        2: "math",
        3: "english",
        4: "python"
    }

    students = []

    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Print student subjects and grades")
        print("3. Calculate average grade for each student")
        print("4. Show students from best to worst average grade")
        print("5. Show student with highest grade and subject")
        print("6. Show student with lowest grade and subject")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            student = Student(name)

            while True:
                print("\nSelect a subject:")
                for num, subject in subjects.items():
                    print(f"{num}. {subject}")

                subject_choice = int(input("Enter subject number (0 to finish): "))
                if subject_choice == 0:
                    break

                if subject_choice not in subjects:
                    print("Invalid subject choice.")
                    continue

                subject_name = subjects[subject_choice]
                grade = float(input(f"Enter grade for {subject_name}: "))
                subject = Subject(subject_name, grade)
                student.subjects.append(subject)

            students.append(student)
            print("Student added successfully!")

        elif choice == "2":
            if not students:
                print("No students to display.")
            else:
                for student in students:
                    print(f"Student: {student.name}")
                    for subject in student.subjects:
                        print(f"Subject: {subject.name}, Grade: {subject.grade}")
                    print()

        elif choice == "3":
            if not students:
                print("No students to calculate average for.")
            else:
                for student in students:
                    grades = [subject.grade for subject in student.subjects]
                    avg_grade = calculate_average(grades)
                    print(f"Student: {student.name}, Average Grade: {avg_grade:.2f}")
            print()

        elif choice == "4":
            if not students:
                print("No students to display.")
            else:
                sorted_students = sorted(students, key=lambda student: calculate_average([subject.grade for subject in student.subjects]), reverse=True)
                for student in sorted_students:
                    avg_grade = calculate_average([subject.grade for subject in student.subjects])
                    print(f"Student: {student.name}, Average Grade: {avg_grade:.2f}")
            print()

        elif choice == "5":
            if not students:
                print("No students to display.")
            else:
                highest_student = max(students, key=lambda student: max([subject.grade for subject in student.subjects], default=0))
                highest_grade = max([subject.grade for subject in highest_student.subjects], default=0)
                highest_subject = next(subject.name for subject in highest_student.subjects if subject.grade == highest_grade)
                print(f"Student with Highest Grade: {highest_student.name}")
                print(f"Subject with Highest Grade: {highest_subject}")
                print(f"Highest Grade: {highest_grade:.2f}")
            print()

        elif choice == "6":
            if not students:
                print("No students to display.")
            else:
                lowest_student = min(students, key=lambda student: min([subject.grade for subject in student.subjects], default=0))
                lowest_grade = min([subject.grade for subject in lowest_student.subjects], default=0)
                lowest_subject = next(subject.name for subject in lowest_student.subjects if subject.grade == lowest_grade)
                print(f"Student with Lowest Grade: {lowest_student.name}")
                print(f"Subject with Lowest Grade: {lowest_subject}")
                print(f"Lowest Grade: {lowest_grade:.2f}")
            print()

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
