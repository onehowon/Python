import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 3, 801)
y = (x+1)**2-1
plt.plot(x,y)
plt.show()

x = np.linspace(-3,5,801)
y = -0.5*(x-1)**2+2
plt.plot(x,y)
plt.show()
