import numpy as np
import matplotlib.pyplot as plt

##### 1번 문제 #####
x = np.linspace(1, 4, 900)
y_1 = 2*x + 3
plt.plot(x,y_1)
plt.show()

##### 2번 문제 #####
x = np.linspace(-4, 4, 100)
y_2 = x**2-2*x+4
plt.plot(x,y_2)
plt.show()