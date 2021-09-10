import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,10,901)
gx =np.sqrt(x-1)
plt.plot(x,gx)
plt.show()