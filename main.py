import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

plt.figure()

# funksjonen fra oppgaven
def f(x):
    return np.exp(-x/4) * np.arctan(x)

# ligningen vi fikk fra f'(x) = 0
def g(x):
    return np.arctan(x) - 4/(x**2 + 1)

# finner x-verdien til toppunktet
x_solution = fsolve(g, 1)

# finner y-verdien
y_solution = f(x_solution)

print("x =", round(x_solution[0],4))
print("y =", round(y_solution[0],4))

# lager x-verdier
x = np.linspace(0,5,500)

# regner ut funksjonsverdier
y = f(x)

# tegner grafen
plt.plot(x, y)

# markerer toppunktet
plt.scatter(x_solution, y_solution, color="red")

plt.savefig("plot.png")