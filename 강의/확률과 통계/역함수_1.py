import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*x-4

def f_inv(x):
    return (x+4)/3

def g(x):
    return x**2+1

def g_inv(x):
    return np.sqrt(x-1)

def identity(x):
    return x

x = np.linspace(-1,5,601)
graph, = plt.plot(x,f(x))
graph1, = plt.plot(x,f_inv(x))
graph2, = plt.plot(x, identity(x), '--')
plt.legend(handles = (graph, graph1, graph2), labels = (r'$y=f(x)$', r'$y=f^{-1}(x)$', r'$y=x$')) 
plt.ylim(-1,5)
plt.show()

x = np.linspace(0,6,601)
graph, = plt.plot(x,g(x))
graph1, = plt.plot(x,g_inv(x))
grahp2, = plt.plot(x, identity(x), '--')
plt.legend(handles = (graph, graph1, graph2), labels =(r'$y=g(x)$', r'$y=g^{-1}(x)$', r'$y=x$'))
plt.ylim(0,6)
plt.show()