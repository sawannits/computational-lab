import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    "Student": [
        "S1",
        "S2",
        "S3",
        "S4",
        "S5",
        "S6",
        "S7",
        "S8",
        "S9",
        "S10",
    ],
    "Mathematics": [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
    "Physics": [72, 88, 70, 92, 75, 79, 68, 90, 74, 85],
    "Chemistry": [75, 82, 65, 88, 78, 83, 72, 92, 79, 86],
    "English": [80, 84, 72, 91, 76, 80, 70, 95, 77, 89],
}

df = pd.DataFrame(data)
print("Dataset Overview:")
print(df)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df[["Mathematics", "Physics", "Chemistry", "English"]], palette="Set2"
)
plt.title("Subject-wise Score Distributions")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.show()

sns.pairplot(df, vars=["Mathematics", "Physics", "Chemistry", "English"], diag_kind='kde', palette="husl")
plt.suptitle("Pairwise Relationships Between Subjects", y=1.02)
plt.show()

plt.figure(figsize=(6, 5))
corr_matrix = df[["Mathematics", "Physics", "Chemistry", "English"]].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Subject Scores")
plt.show()
