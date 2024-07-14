import matplotlib.pyplot as plt
import numpy as np

a=float(input("enter a value for a"))
b=float(input("enter a value for b"))
c=float(input("enter a value for c"))

def quadratic_model( time):

  temperature = a * time**2 + b * time + c
  return temperature
def main():
      time_values = np.linspace(0, 10, 100)
      temperature_hardcoded = quadratic_model(time_values)

      plt.plot(time_values, temperature_hardcoded, label='hardcoded coefficents',marker='*')

      plt.xlabel('Time')
      plt.ylabel('Temperature')
      plt.legend()
      plt.title('Weather Modeling with Quadratic equation ')

      plt.show()
if __name__ == '_main_':
      main()