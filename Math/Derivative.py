from sympy import symbols, Derivative
import numpy as np

x = symbols('x')

# Derivative example 1
f = x ** 2
fprime = Derivative(f, x).doit()

print(f"f(x) = {f}")
print(f"f'(x) = {fprime}", end = "\n\n")

# Derivative example 2
g = x ** 3 + 2 * x ** 2 + 5 * x + 6
gprime = Derivative(g, x).doit()

print(f"g(x) = {g}")
print(f"g'(x) = {gprime}", end = "\n\n")