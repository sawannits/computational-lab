import matplotlib.pyplot as plt

study_hours = [8, 10, 12, 15, 18, 20, 7, 14, 16, 22]
exam_scores = [65, 72, 75, 82, 88, 90, 60, 80, 85, 95]

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.hist(study_hours, bins=5, color='purple', edgecolor='black')
plt.title('Distribution of Study Hours (Histogram)')
plt.xlabel('Study Hours/Week')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.scatter(study_hours, exam_scores, color='green', s=100)
plt.title('Study Hours vs Exam Score (Scatter Plot)')
plt.xlabel('Study Hours/Week')
plt.ylabel('Exam Score')
plt.grid(True)

plt.tight_layout()
plt.show()
