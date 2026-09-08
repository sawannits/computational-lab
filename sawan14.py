import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([6, 17, 34, 57, 86, 121])

def poly(x, a, b, c):
    return a*x**2 + b*x + c

p, _ = curve_fit(poly, x, y)

print("a =", p[0])
print("b =", p[1])
print("c =", p[2])

plt.scatter(x, y, color='red', label='Data')
plt.plot(x, poly(x, *p), label='Fitted curve')
plt.legend()
plt.show()

