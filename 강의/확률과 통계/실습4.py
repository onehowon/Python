import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi)

y1 = 2*np.cos(x) + 4
y2 = -np.sin(4*x) + 7
y3 = 4*np.tan(2*x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()