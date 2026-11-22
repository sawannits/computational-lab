import numpy as np
import math
def calculate1(array):
	print(f"mean, median, standard deviation, minimum, maximum of {array} are:{np.mean(array):.2f},{np.median(array):.2f},{np.std(array):.2f},{np.min(array)},{np.max(array)}\n")
marks1 = [78, 85, 92, 67, 88, 73, 95, 81, 76, 89]
marks=np.array(marks1)
temperatures1 =[28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5]
temperatures=np.array(temperatures1)
sales1= [12500, 13800, 14200, 11900, 15100, 14750, 16000]
sales=np.array(sales1)
print("Using Numpy:\n")
calculate1(marks)
calculate1(temperatures)
calculate1(sales)
print("Without using Numpy:\n")
def calculate2(data):
	mean = sum(data) / len(data)
	sorted_data = sorted(data)
	n = len(sorted_data)
	if n % 2 == 0:
	    median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
	else:
	    median = sorted_data[n // 2]
	variance = sum((x - mean) ** 2 for x in data) / len(data)
	std_dev = math.sqrt(variance)
	minimum = min(data)
	maximum = max(data)
	print(f"mean, median, standard deviation, minimum, maximum of {data} are:{mean:.2f},{median:.2f},{std_dev:.2f},{minimum},{maximum}\n")
calculate2(marks1)
calculate2(temperatures1)
calculate2(sales1)
