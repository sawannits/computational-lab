import sqlite3

con = sqlite3.connect("student.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students(
roll_no INTEGER PRIMARY KEY,
name TEXT NOT NULL,
department TEXT NOT NULL,
cgpa REAL NOT NULL)""")
con.commit()

def add():
    try:
        d = (int(input("Roll No: ")), input("Name: "),
             input("Department: "), float(input("CGPA: ")))
        cur.execute("INSERT INTO students VALUES(?,?,?,?)", d)
        con.commit()
        print("Student added.")
    except sqlite3.IntegrityError:
        print("Roll number already exists.")
    except ValueError:
        print("Invalid input.")

def display():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    if not rows:
        print("No records found.")
    else:
        for r in rows:
            print(r)

def search():
    try:
        n = int(input("Roll No: "))
        cur.execute("SELECT * FROM students WHERE roll_no=?", (n,))
        r = cur.fetchone()
        print(r if r else "Student not found.")
    except ValueError:
        print("Invalid roll number.")

def update():
    try:
        n = int(input("Roll No: "))
        cur.execute("SELECT * FROM students WHERE roll_no=?", (n,))
        if not cur.fetchone():
            print("Student not found.")
            return

        d = (input("New Name: "), input("New Department: "),
             float(input("New CGPA: ")), n)
        cur.execute("""UPDATE students SET name=?,department=?,cgpa=?
                       WHERE roll_no=?""", d)
        con.commit()
        print("Student updated.")
    except ValueError:
        print("Invalid input.")

def delete():
    try:
        n = int(input("Roll No: "))
        cur.execute("DELETE FROM students WHERE roll_no=?", (n,))
        con.commit()
        print("Student deleted." if cur.rowcount else "Student not found.")
    except ValueError:
        print("Invalid roll number.")

while True:
    print("\n1.Add  2.Display  3.Search  4.Update  5.Delete  6.Exit")
    ch = input("Choice: ")

    if ch == "1": add()
    elif ch == "2": display()
    elif ch == "3": search()
    elif ch == "4": update()
    elif ch == "5": delete()
    elif ch == "6": break
    else: print("Invalid choice.")

con.close()
