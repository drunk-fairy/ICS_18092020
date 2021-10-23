import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from math import cos

def f(x):
    return x**(cos(x**2))

x = linspace(0, 10, 100)

f2 = np.vectorize(f)

plt.plot(x, f2(x), 'g-', label = 'x**(cos(x**2))')
plt.legend()
plt.show()