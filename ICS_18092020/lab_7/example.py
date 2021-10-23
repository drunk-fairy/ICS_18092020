from math import sqrt
from numpy import * 
import matplotlib.pyplot as plt

def f(t):
    return t**2
def f1(t1):
    return 2*sqrt(t1)
def f2(t):
    return abs(t)
    
t = linspace(-4, 4, 100)
t1 = linspace(0, 4, 100)
y = f(t)
y1 = f1(t1)
y2 = f2(t)

plt.plot(t, y, 'm-.', label = 't**2')
plt.plot(t1, y1, 'r-', label = '2*sqrt(t1)')
plt.plot(t, y2, 'g:', label = 'abs(t)')

plt.xlabel('вісь x')
plt.ylabel('вісь y')
plt.title('Some plot')
plt.legend()
plt.grid(True)
#plt.savefig('example_plot_1.png', dpi = 200)
plt.show()