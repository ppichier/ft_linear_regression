import matplotlib.pyplot as plt

def showVisu(X, Y, t0, t1):
    Yp = []
    for x in X:
        Yp.append(t0 + t1 * x)
    plt.plot(X, Y, 'bo')
    plt.plot(X, Yp, 'r')
    plt.xlabel("kilometers")
    plt.ylabel("price")
    plt.title('ft_linear_regression')
    plt.grid(alpha=.4,linestyle='--')
    plt.show()

def gradient_descent(X, Y,t0, t1, learning_rate, num_iterations):
    N = len(X)

    for i in range(num_iterations):
        t0_gradient = 0.0 
        t1_gradient = 0.0
        for j in range(N):
            t0_gradient += ((t0 + t1 * X[j]) - Y[j])
            t1_gradient += (((t0 + t1 * X[j]) - Y[j]) * X[j])
        t0 =  t0 - (learning_rate * t0_gradient * 1/float(N))
        t1 =  t1 - (learning_rate * t1_gradient * 1/float(N))
    return [t0,t1]


def normalize(X, Y):
    maxX = float(max(X))
    minX = float(min(X))
    maxY = float(max(Y))
    minY = float(min(Y))
    Xnormalize = list(map((lambda x: (float(x) - minX)/(maxX - minX)), X))
    Ynormalize = list(map((lambda y: (float(y) - minY)/(maxY - minY)), Y))
    return [Xnormalize, Ynormalize]

def denormalize(X, Y, t0_normalize, t1_normalize):
    maxX = float(max(X))
    minX = float(min(X))
    maxY = float(max(Y))
    minY = float(min(Y))
    t1 = t1_normalize * (maxY - minY) / (maxX - minX)
    t0 = t0_normalize * (maxY - minY) + minY - t1 * minX
    return [t0, t1]
    

def cost(X, Y, t0, t1):
    N = len(X)
    error = 0.0
    for i in range(N):
        error += abs((t0 + t1 * X[i]) - Y[i])
    return (error / N)

def train():
    learning_rate = 0.1
    initial_t0 = 0.0
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


    Xn, Yn = normalize(X, Y)
    t0_normalize, t1_normalize = gradient_descent(Xn, Yn, initial_t0, initial_t1, learning_rate, num_iterations)
    t0, t1 = denormalize(X, Y, t0_normalize, t1_normalize)
    print(cost(X, Y, t0, t1))
    print("t0 = {0}".format(t0))
    print("t1 = {0}".format(t1))
    print("t0_normalize = {0}".format(t0_normalize))
    print("t1_normalize = {0}".format(t1_normalize))
    showVisu(Xn, Yn, t0_normalize, t1_normalize)
    showVisu(X, Y, t0, t1)
    return (t0, t1)