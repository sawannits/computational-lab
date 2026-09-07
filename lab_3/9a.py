import numpy as np

marks = np.array([78, 85, 92, 67, 88, 73, 95, 81, 76, 89])

temperatures = np.array(
    [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5]
)

sales = np.array(
    [12500, 13800, 14200, 11900, 15100, 14750, 16000]
)


def statistics(data, name):
    print("\n", name)
    print("Mean:", np.mean(data))
    print("Median:", np.median(data))
    print("Standard Deviation:", np.std(data))
    print("Minimum:", np.min(data))
    print("Maximum:", np.max(data))


statistics(marks, "Marks")
statistics(temperatures, "Temperatures")
statistics(sales, "Sales")
