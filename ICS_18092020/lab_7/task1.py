import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from math import sin

def f(x):
    return x*sin(5*x)

x = linspace(-2, 5, 100)

f2 = np.vectorize(f)

plt.plot(x, f2(x), 'm:', label = 'x*sin(5*x)')
plt.legend()
plt.show()