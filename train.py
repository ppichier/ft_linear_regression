import matplotlib.pyplot as plt
import numpy as np

def showCostVisu(N, C):
    plt.xlabel("iterations")
    plt.ylabel("cost")
    plt.plot(list(range(N)), C, 'b')
    plt.show()

def showRegressionVisu(X, Y, t0, t1, normalize=True):
    Yp = []
    for x in X:
        Yp.append(t0 + t1 * x)
    plt.plot(X, Y, 'bo')
    plt.plot(X, Yp, 'r')
    plt.xlabel("kilometers")
    plt.ylabel("price")
    plt.title('ft_linear_regression')
    if not normalize:
        plt.axis([0, 250000, 0, 9000])
    plt.grid(alpha=.4,linestyle='--')
    plt.show()

def cost(X, Y, t0, t1):
    N = len(X)
    error = 0.0
    for i in range(N):
        error += abs((t0 + t1 * X[i]) - Y[i])
    return (error / N)

def gradient_descent(X, Y,t0, t1, learning_rate, num_iterations):
    N = len(X)
    cost = []

    for i in range(num_iterations):
        t0_gradient = 0.0 
        t1_gradient = 0.0
        e = 0.0
        for j in range(N):
            t0_gradient += ((t0 + t1 * X[j]) - Y[j])
            t1_gradient += (((t0 + t1 * X[j]) - Y[j]) * X[j])
            e += abs((t0 + t1 * X[j]) - Y[j])
        t0 =  t0 - (learning_rate * t0_gradient * 1/float(N))
        t1 =  t1 - (learning_rate * t1_gradient * 1/float(N))
        cost.append(e)
    return [t0, t1, cost]

def normalize(X, Y, initial_t0):
    #Normalize X and Y on 0,1
    Xnormalize = list(map((lambda x: (float(x) - float(min(X)))/(float(max(X)) - float(min(X)))), X))
    Ynormalize = list(map((lambda y: (float(y) - float(min(Y)))/(float(max(Y)) - float(min(Y)))), Y))
    #Normalize initial value of t0
    t0 = (float(initial_t0) - float(min(X)))/(float(max(X) - float(min(X))))
    return [Xnormalize, Ynormalize, t0]

def denormalize(X, Y, t0_normalize, t1_normalize):
    t1 = t1_normalize * (float(max(Y)) - float(min(Y))) / (float(max(X)) - float(min(X)))
    t0 = t0_normalize * (float(max(Y)) - float(min(Y))) +float(min(Y)) - t1 * float(min(X))
    return [t0, t1]

def train():
    learning_rate = 0.1
    initial_t0 = 1.0
    initial_t1 = 0.0
    num_iterations = 1000
    try:
        with open('data.csv', 'r') as f:
            X = []
            Y = []
            for i in range(1):
                f.readline()
            for line in f:
                line = line.rstrip()
                words = line.split(',')
                X.append(float(words[0]))
                Y.append(float(words[1]))
    except Exception as e:
        raise Exception(e)

    Xn, Yn, initial_t0 = normalize(X, Y, initial_t0)
    t0_normalize, t1_normalize, C = gradient_descent(Xn, Yn, initial_t0, initial_t1, learning_rate, num_iterations)
    t0, t1 = denormalize(X, Y, t0_normalize, t1_normalize)

    try:
        f = open("thetas.csv", "w+")
        f.write(str(t0) + "," + str(t1))
        f.close()
    except Exception as e:
        raise Exception(e)

    print("theta0 = {0:.3f}".format(t0))
    print("theta1 = {0:.3f}".format(t1))
    print("Average error: {0:.3f}".format(cost(X, Y, t0, t1)))

    showRegressionVisu(Xn, Yn, t0_normalize, t1_normalize)
    showRegressionVisu(X, Y, t0, t1, False)
    showCostVisu(num_iterations, C)

if __name__== '__main__':
    train()