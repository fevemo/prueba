import numpy as np
import matplotlib.pyplot as plt

y0=1
t0=0
tf=5
n=1000
t=np.linspace(t0,tf,n)

def f(t,y):
    return -y

def euler():
    y=np.zeros(n)
    y[0]=y0
    deltat=t[1]-t[0]
    for i in range(n-1):
       slope= f(t[i],y[i])
       y[i+1]=y[i]+deltat*slope
    return y

y=euler()

ye=np.exp(-t)

plt.plot(t,y)
plt.plot(t,ye)
plt.show()
