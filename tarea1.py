import numpy as np
import matplotlib.pyplot as plt

p=28
s=10
b=8./3

def dxdt(t,x,y,z):
    return s*(y-x)
def dydt(t,x,y,z):
    return x*(p-z)-y
def dzdt(t,x,y,z):
    return x*y-b*z

t0=0
tf=40
N=5000
t=np.linspace(t0,tf,N)

X=np.zeros(N)
Y=np.zeros(N)
Z=np.zeros(N)
X[0]=2
Y[0]=3
Z[0]=4

deltat=t[1]-t[0]
for i in range(N-1):
    s1x= dxdt(t[i],X[i],Y[i],Z[i])
    s1y= dydt(t[i],X[i],Y[i],Z[i])
    s1z= dzdt(t[i],X[i],Y[i],Z[i])

    Xm=X[i]+deltat/2*s1x
    Ym=Y[i]+deltat/2*s1y
    Zm=Z[i]+deltat/2*s1z
    tm=t[i]+deltat/2

    s2x=dxdt(tm,Xm,Ym,Zm)
    s2y=dydt(tm,Xm,Ym,Zm)
    s2z=dzdt(tm,Xm,Ym,Zm)

    X[i+1]=X[i]+deltat*s2x
    Y[i+1]=Y[i]+deltat*s2y
    Z[i+1]=Z[i]+deltat*s2z

plt.plot(X,Y)
plt.title("X vs Y")
plt.show()
plt.plot(Y,Z)
plt.title("Y vs Z")
plt.show()
plt.plot(X,Z)
plt.title("X vs Z")
plt.show()
