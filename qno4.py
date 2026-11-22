student1 = (101, "Alice")
student2 = (102, "Bob")
courses_student1 = {"Python", "Data Structures", "Mathematics", "AI"}
courses_student2 = {"Python", "Database", "AI", "Networking"}

print("Student Details")
print("Student 1:", student1)
print("Student 2:", student2)
print("\n Courses Enrolled")
print(student1[1], ":", courses_student1)
print(student2[1], ":", courses_student2)

all_courses = courses_student1.union(courses_student2)
common_courses = courses_student1.intersection(courses_student2)

unique_to_student1 = courses_student1.difference(courses_student2)
unique_to_student2 = courses_student2.difference(courses_student1)

print("\n Course Analysis")
print("All Courses (Union):", all_courses)
print("Common Courses (Intersection):", common_courses)
print("Courses only for", student1[1], "(Difference):", unique_to_student1)
print("Courses only for", student2[1], "(Difference):", unique_to_student2)
