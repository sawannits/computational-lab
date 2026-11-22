def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    elif avg >= 50:
        return "E"
    else:
        return "F"

with open("students.txt", "r") as infile, open("results.txt", "w") as outfile:
    outfile.write("RollNo\tName\tTotal\tAverage\tGrade\n")
    
    for line in infile:
        data = line.split()

        roll = data[0]
        name = data[1]
        marks =list(map(int,data[2:]))
        total = sum(marks)
        average = total / len(marks)
        grade = get_grade(average)

        outfile.write(f"{roll}\t{name}\t{total}\t{average:.2f}\t{grade}\n")

print("Student results have been written to 'results.txt'.")
