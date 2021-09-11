import numpy as np
import matplotlib.pyplot as plt

x1 =np.linspace(0.1,4,401)
y1 =np.log2(x1)
x2 = np.linspace(-0.9, 4, 501)
y2 = np.log2(x2+1)-1

graph1, = plt.plot(x1,y1)
graph2, = plt.plot(x2,y2)
plt.legend(handles = (graph1, graph2), labels = (r'$y=log_2(x)$', r'$y=log_2(x+1)-1$'))
plt.show()