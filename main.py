# ==============================
# Student Course Tracker
# Starter Template
# ==============================

# Starter data (DO NOT MODIFY)
students = [
    ("Alice", 20),
    ("Bob", 22),
    ("Charlie", 21)
]

courses = ["Python", "JavaScript", "Python", "Databases"]

student_data = {
    "Alice": {"courses": ["Python", "Databases"], "grades": [85, 90]},
    "Bob": {"courses": ["Python", "JavaScript"], "grades": [78, 82]},
    "Charlie": {"courses": ["JavaScript"], "grades": [88]}
}

# ------------------------------
# Task 1: Remove Duplicate Courses
# ------------------------------
# TODO:
# - Convert the courses list into a set
# - Print the unique courses
new_courses = set(courses)
print("New courses:", new_courses)

# ------------------------------
# Task 2: Display Student Info
# ------------------------------
# TODO:
# - Loop through the students list
# - For each student, print:
#   Name, age, and enrolled courses
for name, age in students:
    enrolled_courses = student_data[name]["courses"]
    print(f"Name: {name}, Age: {age}, Courses: {enrolled_courses}")


# ------------------------------
# Task 3: Add Course for Bob
# ------------------------------
# TODO:
# - Add "Databases" to Bob's course list
#   ONLY if he is not already enrolled
# - Print Bob's updated course list
if "Databases" not in student_data["Bob"]["courses"]:
    student_data["Bob"]["courses"].append("Databases")
print("Bob's updated courses:", student_data["Bob"]["courses"])


# ------------------------------
# Task 4: Calculate Average Grades
# ------------------------------
# TODO:
# - Loop through student_data
# - Calculate and print each student's average grade
for name, info in student_data.items():
    grades = info["grades"]
    average = sum(grades) / len(grades)
    print(f"{name}'s average grade: {average}")


# ------------------------------
# Task 5: Find Students in a Course
# ------------------------------
# TODO:
# - Ask the user to enter a course name
# - Print all students enrolled in that course
course_name = input("Enter a course name to find enrolled students: ").lower()
for name, info in student_data.items():
    if course_name in [course.lower() for course in info["courses"]]:
        print(name)

# ------------------------------
# Bonus (Optional)
# ------------------------------
# TODO:
# - Store each student's average grade in the dictionary
# - Print the student with the highest average grade
highest_avg = 0
top_student = ""  
for name, info in student_data.items():
    grades = info["grades"]
    average = sum(grades) / len(grades)
    info["average"] = average  # store average in dictionary
    if average > highest_avg:
        highest_avg = average
        top_student = name

print(f"Top student: {top_student} with an average grade of {highest_avg}")