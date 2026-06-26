 #######################################################################################
# Day -2 : A student grade tracker that:

# Stores 5 students with their marks in a dictionary
# Loops through and prints each student's name and mark
# Finds and prints the highest scorer
# Finds and prints the lowest scorer
# Calculates and prints the class average
 #######################################################################################

def input_student_info():
    roll_number = input("Enter the roll number of the student: ")
    name = input("Enter the name of the student: ")
    marks = int(input("Etner the mark of the student: "))
    student = dict(student_name = name, student_roll = roll_number, student_marks = marks)

    return student

students = []

for i in range(3):
    student = input_student_info()
    students.append(student)

for i in range(len(students)):
    print(students[i])

highest_marks = students[0].get("student_marks")
for i in range(len(students)):
    if students[i].get("student_marks") > highest_marks:
        highest_marks = students[i].get("student_marks")

print(f"The highest marks among all the students is {highest_marks}")

lowest_marks = students[0].get("student_marks")
for i in range(len(students)):
    if students[i].get("student_marks") < lowest_marks:
        lowest_marks = students[i].get("student_marks")

print(f"The lowest marks among all the students is {lowest_marks}")

total_marks = 0
for i in range(len(students)):
    total_marks = students[i].get("student_marks")+total_marks

print(f"the average marks of the class is {total_marks/len(students)}")
    