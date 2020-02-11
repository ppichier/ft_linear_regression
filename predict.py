import numpy as np
import matplotlib.pyplot as plt
from train import train

def predict(km, theta0, theta1):
    return theta0 + theta1 * km


def run():
    a = input("Enter number of kilometers: ")
    try:
        km = float(a)
        if km < 0: # max ?
            print("Number is not valid")
            return
    except ValueError as e:
        print(e)
        return
    try:
        [t0, t1] = train()
    except Exception as e:
        print(e)
        return
    
    # print("theta0 = {0}".format(t0))
    # print("theta1 = {0}".format(t1))
    res = predict(km, t0, t1)
    print(res)

if __name__== '__main__':
    run()