students = []

name = input("Enter student name: ")

try:
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    student = (name, age, marks)

    students.append(student)

    print("\nStudent Record:")
    print(students)

except ValueError:
    print("Please enter numbers only for age and marks")