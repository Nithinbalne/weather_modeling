import numpy as np
import matplotlib.pyplot as plt

a=0.2
b=1
c=40
x=np.linspace(1,10,100)
y=a*x**2 + b*x +c


q=-0.1
p=1
r=20
w=np.linspace(1,10,100)
z=q*w**2 + p*w +r
plt.plot(x,y,c="black",lw=2)
plt.plot(w,z,c="blue",lw=2)

plt.xlabel('time (hr)')
plt.ylabel('temperature (°C)')
plt.title('multiple inputs')
plt.show()