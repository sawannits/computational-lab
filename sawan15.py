from scipy.optimize import minimize

def f(variables):
    x, y = variables
    return (x - 2)**2 + (y - 2)**2

initial_guess = [0, 0]

result = minimize(f, initial_guess)

print("Minimum value:", result.fun)
print("Optimal x:", result.x[0])
print("Optimal y:", result.x[1])

