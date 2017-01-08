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


def leapfrog():
    y=np.zeros(n)
    y[0]=y0
    deltat=t[1]-t[0]
    y[1]=y[0]+deltat*f(t[0],y[0])
    for i in range(n-2):
       slope= f(t[i],y[i])
       y[i+2]=y[i]+deltat*slope*2
    return y

def rk2():
    y=np.zeros(n)
    y[0]=y0
    deltat=t[1]-t[0]
    for i in range(n-1):
       slope= f(t[i],y[i])
       y1=y[i]+deltat/2*slope
       midslope=f(t[i]+deltat/2,y1)
       y[i+1]=y[i]+deltat*midslope     
    return y

def rk4():
    y=np.zeros(n)
    y[0]=y0
    deltat=t[1]-t[0]
    for i in range(n-1):
       s1= f(t[i],y[i])
       s2=f(t[i]+deltat/2 , y[i]+deltat/2*s1)
       s3=f(t[i]+deltat/2 , y[i]+deltat/2*s2)
       s4=f(t[i]+deltat , y[i]+deltat*s3)
       y[i+1]=y[i]+deltat*(s1+2*s2+2*s3+s4)/6.     
    return y

ye=euler()
ylf=leapfrog()
yrk2=rk2()
yrk4=rk4()
yr=np.exp(-t)

plt.plot(t,ye, label="Euler")
plt.plot(t,ylf,label="LeapFrog")
plt.plot(t,yrk2,label="RK2")
plt.plot(t,yrk4,label="RK4")
plt.plot(t,yr,label="Real")
plt.legend()
plt.show()
