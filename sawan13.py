from scipy.integrate import quad

def f(x):
    return x**2 + 2*x + 1

h = 0.000001
d = (f(2 + h) - f(2 - h)) / (2 * h)
print("Derivative at x=2:", d)

I, error = quad(f, 0, 2)
print("Integration:", I)
 
