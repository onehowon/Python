import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,np.pi-1,501)
y=np.sin(2*(x+1))
plt.plot(x,y)
plt.show()

x = np.linspace(0,2*np.pi,501)
y = -3*np.cos(x)+1
plt.plot(x,y)
plt.show()