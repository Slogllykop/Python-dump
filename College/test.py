import numpy as np 
import matplotlib.pyplot as plt

x=np.linspace(-3,3,100)
def f(x): return x**2
plt.plot(x,f(x))