# Student Result Management System

students_list = []

for i in range(5):
    print("Student", i + 1, "ki details enter karo:")
    name = input("Enter Name: ")
    roll_no = input("Enter Roll No: ")
    
    # Marks for 3 subjects
    python = float(input("Python Marks: "))
    ai = float(input("AI Marks: "))
    math = float(input("Math Marks: "))
    
    total = python + ai + math
    percentage = (total / 300) * 100
    
    if percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 50:
        grade = 'D'
    else:
        grade = 'F'
        
    student_data = {
        "name": name,
        "roll": roll_no,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }
    
    students_list.append(student_data)
    print()

print(" All Students Results ")

file_text = "Student Results\n\n"
highest_per = 0
top_student_name = ""

for s in students_list:
    line = "Name: " + s["name"] + ", Roll No: " + s["roll"] + ", Total: " + str(s["total"]) + "/300, Percentage: " + str(round(s["percentage"], 2)) + "%, Grade: " + s["grade"]
    print(line)
    file_text = file_text + line + "\n"
    
    if s["percentage"] > highest_per:
        highest_per = s["percentage"]
        top_student_name = s["name"]

top_line = "\nHighest Percentage: " + top_student_name + " with " + str(round(highest_per, 2)) + "%"
print(top_line)
file_text = file_text + top_line

f = open("results.txt", "w")
f.write(file_text)
f.close()

print("\nData results.txt file mein save ho gaya hai!")