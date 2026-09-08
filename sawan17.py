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

def add():
    try:
        data = (
            int(input("ID: ")),
            input("Name: "),
            input("Designation: "),
            input("Department: "),
            float(input("Salary: "))
        )
        cur.execute("INSERT INTO employee VALUES (?,?,?,?,?)", data)
        con.commit()
        print("Employee added.")
    except sqlite3.IntegrityError:
        print("ID already exists.")

def display():
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    if not rows:
        print("No records found.")
    else:
        for r in rows:
            print(r)

def update():
    try:
        id = int(input("Enter ID to update: "))
        cur.execute("SELECT * FROM employee WHERE id=?", (id,))
        if not cur.fetchone():
            print("Employee not found.")
            return

        data = (
            input("New Name: "),
            input("New Designation: "),
            input("New Department: "),
            float(input("New Salary: ")),
            id
        )
        cur.execute("""
            UPDATE employee
            SET name=?, designation=?, department=?, salary=?
            WHERE id=?
        """, data)
        con.commit()
        print("Employee updated.")
    except ValueError:
        print("Invalid input.")

def delete():
    id = int(input("Enter ID to delete: "))
    cur.execute("DELETE FROM employee WHERE id=?", (id,))
    con.commit()
    print("Employee deleted." if cur.rowcount else "Employee not found.")

while True:
    print("\n1.Add  2.Display  3.Update  4.Delete  5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add()
    elif ch == "2":
        display()
    elif ch == "3":
        update()
    elif ch == "4":
        delete()
    elif ch == "5":
        break
    else:
        print("Invalid choice.")

con.close()
