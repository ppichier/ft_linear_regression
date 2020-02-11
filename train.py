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
        # if abs(learning_rate * t0_gradient) <= 0.001 and abs(learning_rate * t1_gradient) <= 0.001 :
        #     return[t0, t1]
    return [t0,t1]


def normalize(X, Y):
    maxX = float(max(X))
    minX = float(min(X))
    maxY = float(max(Y))
    minY = float(min(Y))
    Xnormalize = list(map((lambda x: (float(x) - minX)/(maxX - minX)), X))
    Ynormalize = list(map((lambda y: (float(y) - minY)/(maxY - minY)), Y))
    print(Xnormalize)
    print(Ynormalize)
    return [Xnormalize, Ynormalize]

def denormalize(X, Y, t0_normalize, t1_normalize):
    maxX = float(max(X))
    minX = float(min(X))
    maxY = float(max(Y))
    minY = float(min(Y))
    # A and B normalize to denormalize
    x_a = 0.0
    x_b = 1.0
    y_a = t0_normalize + t1_normalize * 0.0
    y_b = t0_normalize + t1_normalize * 1.0
    x_a_denormalize = x_a * (maxX - minX) + minX
    x_b_denormalize = x_b * (maxX - minX) + minX
    y_a_denormalize = y_a * (maxY - minY) + minY
    y_b_denormalize = y_b * (maxY - minY) + minY

    #find the slope m
    m = (y_b_denormalize - y_a_denormalize) / (x_b_denormalize - x_a_denormalize)
    #point slope formula
    print(y_a)
    print(y_a_denormalize)
    print(y_b)
    print(y_b_denormalize)
    print(maxY)
    print(maxX)
    return [y_a_denormalize, m]
    

    



def train():
    learning_rate = 0.1
    initial_t0 = 0.0
    initial_t1 = 0.0
    num_iterations = 5000
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

    print("t0 = {0}".format(t0))
    print("t1 = {0}".format(t1))
    # showVisu(Xn, Yn, t0_normalize, t1_normalize)
    showVisu(X, Y, t0, t1)
    return (t0, t1)