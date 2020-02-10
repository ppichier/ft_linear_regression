import numpy as np
import matplotlib.pyplot as plt
from train import train

def predict(km, theta0, theta1):
    return theta0 + theta1 * km


def run():
    a = input("Enter number of kilometers: ")
    try:
        km = float(a)
    except ValueError as e:
        print(e)
        return
    #calcul of theta0 and theta1
    try:
        [t0, t1, visu] = train()
    except Exception as e:
        print(e)
        return
    
    print("theta0 = {0}".format(t0))
    print("theta1 = {0}".format(t1))
    # res = predict(km, t0, t1)
    
    # Visu
    x = np.array(range(50))
    # y = t0 + t1 * x #t0 - t1 * km # intercept + slope * x
    y = t0 + t1 * x
    plt.plot(x, y)
    # plt.plot(x, y, '-r', label='y=θ0+θ1*kilometers')
    plt.plot(visu[0], visu[1], 'bo')
    plt.axis([0, 50, 0, 50])
    plt.xlabel("kilometers")
    plt.ylabel("price")
    plt.title('ft_linear_regression')
    plt.grid(alpha=.4,linestyle='--')
    plt.show()

if __name__== '__main__':
    run()