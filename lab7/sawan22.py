import xml.etree.ElementTree as ET

# XML file ko parse karna
tree = ET.parse("university.xml")
root = tree.getroot()

# University details
print("=" * 70)
print("UNIVERSITY INFORMATION")
print("=" * 70)

print("University Name :", root.get("name"))

# Campus details
campus = root.find("campus")

print("\nCAMPUS INFORMATION")
print("-" * 70)
print("Location        :", campus.findtext("location"))
print("Established     :", campus.findtext("established"))
print("Website         :", campus.findtext("website"))

# Departments ko read karna
for department in root.findall("./departments/department"):

    dept_id = department.get("id")
    dept_name = department.findtext("name")
    hod = department.findtext("hod")
    building = department.findtext("building")

    print("\n" + "=" * 70)
    print("DEPARTMENT INFORMATION")
    print("=" * 70)

    print("Department ID   :", dept_id)
    print("Department Name :", dept_name)
    print("HOD             :", hod)
    print("Building        :", building)

    students = department.findall("./students/student")

    print("Number of Students:", len(students))

    # Students ko read karna
    for student in students:

        student_id = student.get("id")

        personal = student.find("personal_details")
        name = personal.find("name")

        first_name = name.findtext("first_name")
        last_name = name.findtext("last_name")

        gender = personal.findtext("gender")
        dob = personal.findtext("date_of_birth")
        phone = personal.findtext("phone")
        email = personal.findtext("email")

        address = personal.find("address")

        street = address.findtext("street")
        city = address.findtext("city")
        state = address.findtext("state")
        postal_code = address.findtext("postal_code")

        academic = student.find("academic_details")

        year = academic.findtext("year")
        semester = academic.findtext("semester")
        cgpa = academic.findtext("cgpa")
        advisor = academic.findtext("advisor")

        print("\n" + "-" * 70)
        print("STUDENT INFORMATION")
        print("-" * 70)

        print("Student ID      :", student_id)
        print("Name            :", first_name, last_name)
        print("Gender          :", gender)
        print("Date of Birth   :", dob)
        print("Phone           :", phone)
        print("Email           :", email)

        print("Address         :", street)
        print("City            :", city)
        print("State           :", state)
        print("Postal Code     :", postal_code)

        print("Year            :", year)
        print("Semester        :", semester)
        print("CGPA            :", cgpa)
        print("Advisor         :", advisor)

        # Courses display karna
        print("\nCOURSES")
        print("-" * 70)

        for course in academic.findall("./courses/course"):

            code = course.get("code")
            course_name = course.findtext("name")
            credits = course.findtext("credits")
            marks = course.findtext("marks")
            grade = course.findtext("grade")

            print("Course Code     :", code)
            print("Course Name     :", course_name)
            print("Credits         :", credits)
            print("Marks           :", marks)
            print("Grade           :", grade)
            print("-" * 40)

print("\n" + "=" * 70)
print("XML DATA PARSING COMPLETED SUCCESSFULLY")
print("=" * 70)

