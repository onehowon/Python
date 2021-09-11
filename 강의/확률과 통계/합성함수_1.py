import numpy as np

def f(x):
    return x**3 + 1

def g(x):
    return np.sqrt(x+2)

print("(g o f)(2) =", g(f(2)))
print("(f o g)(2) =", f(g(2)))
print("(g o g)(2) =", g(g(2)))