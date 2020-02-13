import numpy as np
import matplotlib.pyplot as plt
from train import train

def predict():
    a = input("Enter number of kilometers: ")
    try:
        km = float(a)
        if km < 0 or km > 380000:
            print("Number must be between 0 and 380000")
            return
    except ValueError as e:
        print(e)
        return
    try:
        f = open("thetas.csv", "r")
        thetas = f.readline().split(',')
        t0 = float(thetas[0])
        t1 = float(thetas[1])
    except Exception as e:
        print(e)
        return
    
    
    price = t0 + t1 * km
    print("The predicted price for {0} kilometer(s) is {1:.2f}".format(km, price))

if __name__== '__main__':
    predict()