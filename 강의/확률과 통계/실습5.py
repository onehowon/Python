import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 10000)

def f(x):
    return np.sin(x)

def t1(x):
    return x

def t2(x):
    return t1(x)-(1/6)*x**3

def t3(x):
    return t2(x)-(1/120)*x**5

def t4(x):
    return t3(x)-(1/5040)*x**7

y = f(x)
y1 = t1(x)
y2 = t2(x)
y3 = t3(x)
y4 = t4(x)

graph, = plt.plot(x,y)
graph1, = plt.plot(x,y1)
graph2, = plt.plot(x,y2)
graph3, = plt.plot(x,y3)
graph4, = plt.plot(x,y4)

plt.legend(handles =(graph, graph1,graph2,graph3, graph4), labels=(r'$y=sin(x)$', r'$y=t1(x)$',r'$y=t2(x)$',r'$y=t3(x)$',r'$y=t4(x)$'))
plt.show()


