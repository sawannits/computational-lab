import math

marks = [78, 85, 92, 67, 88, 73, 95, 81, 76, 89]

temperatures = [
    28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5
]

sales = [
    12500, 13800, 14200, 11900,
    15100, 14750, 16000
]


def calculate_statistics(data, name):

    # Mean
    mean = sum(data) / len(data)

    # Sorting for median
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        median = (
            sorted_data[n // 2 - 1] +
            sorted_data[n // 2]
        ) / 2
    else:
        median = sorted_data[n // 2]

    # Variance
    variance = sum(
        (x - mean) ** 2 for x in data
    ) / len(data)

    # Standard deviation
    standard_deviation = math.sqrt(variance)

    # Minimum and maximum
    minimum = min(data)
    maximum = max(data)

    print("\n", name)
    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", standard_deviation)
    print("Minimum:", minimum)
    print("Maximum:", maximum)


calculate_statistics(marks, "Marks")
calculate_statistics(temperatures, "Temperatures")
calculate_statistics(sales, "Sales")
