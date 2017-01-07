import matplotlib.pyplot as plt
import numpy as np

a=np.array([1,2,3,4,5,6])
b=2*a+2
plt.scatter(a,b, c="r")
plt.xlabel("Tiempo")
plt.show()
