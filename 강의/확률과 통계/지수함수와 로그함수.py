import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,2,301)
y1 = 3**x
y2 = 3**(x-1)+2

graph1, = plt.plot(x,y1)
graph2, = plt.plot(x,y2)
plt.legend(handles = (graph1, graph2), labels = (r'$y=3^x$', r'$y=3^{x-1}+2$'))
plt.show()

graph1, = plt.plot(x, y1)
graph2, = plt.plot(x, y2)
plt.legend(handles =(graph1, graph2), labels = (r'$y=3^x$', r'$y=3^{x-1}+2$'))
plt.show()

x = np.linspace(-1,2,301)
y1 = 2**(-x)
y2 = -2**(-x-2)

graph1, = plt.plot(x,y1)
graph2, = plt.plot(x,y2)
plt.legend(handles=(graph1, graph2), labels=(r'$y=2^{-x}$', r'$y=-2^{-x-2}$'))
plt.show()
