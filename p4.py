#Read from a file

import matplotlib.pyplot as plt
import numpy as np
def quadratic_model(time):
  with open('tmp.txt','r')as f:
    a=float(f.readline())
    b=float(f.readline())
    c=float(f.readline())


  temperature = a*time**2 + b*time + c
  return temperature


def main():
  time_values = np.linspace(0,10,100)
  temperature_hardcoded = quadratic_model(time_values)
  plt.plot(time_values, temperature_hardcoded, label='Hard-coded coefficients',marker= '*')
  plt.xlabel('Time in hrs')
  plt.ylabel('Temperature in celsius')
  # plt.legend()
  plt.title('weather Modeling with quadratic equation (hard-coded coefficients)')

  plt.show()

if __name__ == '__main__':
  main()