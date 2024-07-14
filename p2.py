import numpy as np
import matplotlib.pyplot as plt

a=1
b=4
c=3
x=np.linspace(0.1,10,100)
y=a*x**2 + b*x +c
plt.plot(x,y,c="black",lw=2)
plt.ylim(0,)
plt.xlabel('time(s)')  
plt.ylabel('temp(c)')  

plt.title('Quadratic Equation')
plt.show()
#0 10 10 smooth
#-5 5 100