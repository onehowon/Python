import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 100, 500)
y = (np.log(x)/np.log(3))**2 - np.log(x**4)/np.log10(3) + 3

plt.plot(x,y)
plt.show()
