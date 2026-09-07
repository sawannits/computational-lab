import numpy as np

# Mid-semester marks
mid = np.array([
    [65, 70, 68, 72],
    [78, 75, 80, 77],
    [55, 60, 58, 62],
    [82, 85, 80, 88],
    [70, 68, 72, 74]
])

# End-semester marks
end = np.array([
    [72, 78, 75, 80],
    [84, 82, 86, 83],
    [65, 68, 66, 70],
    [88, 90, 85, 92],
    [78, 75, 80, 82]
])

students = ["S1", "S2", "S3", "S4", "S5"]

# Total marks
mid_total = np.sum(mid, axis=1)
end_total = np.sum(end, axis=1)

# Average marks
mid_average = np.mean(mid, axis=1)
end_average = np.mean(end, axis=1)

# Percentage improvement
improvement = ((end_total - mid_total) / mid_total) * 100

print("Student\tMid Total\tEnd Total\tMid Avg\tEnd Avg\tImprovement")

for i in range(len(students)):
    print(
        f"{students[i]}\t"
        f"{mid_total[i]}\t\t"
        f"{end_total[i]}\t\t"
        f"{mid_average[i]:.2f}\t"
        f"{end_average[i]:.2f}\t"
        f"{improvement[i]:.2f}%"
    )
