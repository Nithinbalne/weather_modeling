# multiple set of inputs
import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a_list, b_list, c_list):
    temperatures = []
    num_sets = 2

    for i in range(num_sets):
        a = a_list[i]
        b = b_list[i]
        c = c_list[i]
        temperature = a * time**2 + b * time + c
        temperatures.append(temperature)

    return temperatures

def main():
    num_sets = 2

    a_list = []
    b_list = []
    c_list = []

    for i in range(num_sets):
        a = float(input(f"Enter a value for set {i+1}: "))
        b = float(input(f"Enter b value for set {i+1}: "))
        c = float(input(f"Enter c value for set {i+1}: "))
        a_list.append(a)
        b_list.append(b)
        c_list.append(c)

    time_values = np.linspace(0, 10, 100)
    temperatures = quadratic_model(time_values, a_list, b_list, c_list)

    for i in range(num_sets):
        label = f'Set {i+1} coefficients'
        plt.plot(time_values, temperatures[i], label=label, marker='*')

    plt.xlabel('Time in hrs')
    plt.ylabel('Temperature in celsius')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation (Multiple Sets of Coefficients)')

    plt.show()

if __name__ == '__main__':
    main()
