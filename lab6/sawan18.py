import sqlite3

con = sqlite3.connect("employee.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employee(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    designation TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")
con.commit()

def add_employee():
    data = (
        int(input("Employee ID: ")),
        input("Name: "),
        input("Designation: "),
        input("Department: "),
        float(input("Salary: "))
    )

    cur.execute(
        "INSERT INTO employee VALUES (?,?,?,?,?)", data
    )
    con.commit()
    print("Employee added.")

def salary_report():
    dept = input("Enter Department: ")

    cur.execute("""
        SELECT department, COUNT(*), SUM(salary), AVG(salary)
        FROM employee
        WHERE department = ?
        GROUP BY department
    """, (dept,))

    row = cur.fetchone()

    if row:
        print("\nDepartment-wise Salary Report")
        print("Department :", row[0])
        print("Employees  :", row[1])
        print("Total Salary:", row[2])
        print("Average Salary:", round(row[3], 2))
    else:
        print("No employees found.")

while True:
    print("\n1. Add Employee")
    print("2. Salary Report")
    print("3. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_employee()
    elif ch == "2":
        salary_report()
    elif ch == "3":
        break
    else:
        print("Invalid choice.")

con.close()

