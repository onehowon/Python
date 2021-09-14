import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-1, 1)
x2 = np.linspace(1, 3)
x3 = np.linspace(4 , 5)

y1 = -x1**2 + 2
y2 = x2**2 - 4*x2 + 3
y3 = -x2**2 + 8*x2 - 14

graph1, =plt.plot(x1, y1)
graph2, = plt.plot(x2, y2)
graph3, = plt.plot(x3, y3)
plt.legend(handles=(graph1, graph2, graph3), labels = (r'$y=-x^2+2$', r'$y=x^2-4x+3$', r'$y=-x^2+8x-14$'))
plt.show()
