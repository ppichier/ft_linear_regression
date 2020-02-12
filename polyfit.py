import matplotlib.pyplot as plt
import numpy as np

def showVisu(X, Y, t0, t1):
    Yp = []
    for x in X:
        Yp.append(t0 + t1 * x)
    plt.plot(X, Y, 'bo')
    plt.plot(X, Yp, 'r')
    plt.xlabel("kilometers")
    plt.ylabel("price")
    # plt.axis([0, 250000, 0, 9000])
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
    y_a = t0_normalize + t1_normalize * x_a
    x_a_denormalize = x_a * (maxX - minX) + minX
    y_a_denormalize = y_a * (maxY - minY) + minY

    x_b = 1.0
    y_b = t0_normalize + t1_normalize * x_b
    x_b_denormalize = x_b * (maxX - minX) + minX
    y_b_denormalize = y_b * (maxY - minY) + minY

    #find the slope m
    m = (y_b_denormalize - y_a_denormalize) / (x_b_denormalize - x_a_denormalize)
    #point slope formula
    print("X_a = {0}".format(x_a))
    print("Y_a = {0}".format(y_a))
    print("X_a_denormalize = {0}".format(x_a_denormalize))
    print("Y_a_denormalize = {0}".format(y_a_denormalize))
    print("X_b = {0}".format(x_b))
    print("Y_b = {0}".format(y_b))
    print("X_b_denormalize = {0}".format(y_b_denormalize))
    print("Y_b_denormalize = {0}".format(y_b_denormalize))
    return [y_a_denormalize, m]
    




if __name__== '__main__':
    learning_rate = 0.1
    initial_t0 = 0.0
    initial_t1 = 0.0
    num_iterations = 2000
    # try:
    #     with open('data.csv', 'r') as f:
    #         X = []
    #         Y = []
    #         for i in range(1):
    #             f.readline()
    #         for line in f:
    #             line = line.rstrip()
    #             words = line.split(',')
    #             X.append(float(words[0]))
    #             Y.append(float(words[1]))
    # except Exception as e:
    #     raise Exception(e)
    points = np.genfromtxt('polyfit.csv', delimiter=",")
    X = np.array([240000, 139800, 150500, 185530, 176000, 114800, 166800, 89000, 144500, 84000, 82029, 63060, 74000, 97500, 67000, 76025, 48235, 93000, 60949, 65674, 54000, 68500, 22899, 61789])
    Y = np.array([3650, 3800, 4400, 4450, 5250, 5350, 5800, 5990, 5999, 6200, 6390, 6390, 6600, 6800, 6800, 6900, 6900, 6990, 7490, 7555, 7990, 7990, 7990, 8290])
    
    Xn = np.array([1.0, 0.5384636643774096, 0.5877494806564687, 0.7491029520822106, 0.7052063325364692, 0.4233098880244679, 0.6628297428385866, 0.30447119082823204, 0.5601125743317626, 0.2814404355576437, 0.27236171182997776, 0.18498763248441968, 0.23537892501646698, 0.3436234747882322, 0.2031358676376433, 0.24470638090105526, 0.11670144310712526, 0.32289579504470267, 0.1752640476091773, 0.1970281113398833, 0.1432559039341136, 0.2100450942188198, 0.0, 0.17913321449463615])
    Yn = np.array([0.0, 0.032327586206896554, 0.16163793103448276, 0.1724137931034483, 0.3448275862068966, 0.36637931034482757, 0.46336206896551724, 0.5043103448275862, 0.50625, 0.5495689655172413, 0.5905172413793104, 0.5905172413793104, 0.6357758620689655, 0.6788793103448276, 0.6788793103448276, 0.7004310344827587, 0.7004310344827587, 0.7198275862068966, 0.8275862068965517, 0.8415948275862069, 0.9353448275862069, 0.9353448275862069, 0.9353448275862069, 1.0])
    z1 = np.polyfit(X, Y, 1)
    print(z1)
    z2 = np.polyfit(Xn, Yn, 1)
    print(z2)
    print("END")


    # Xn, Yn = normalize(X, Y)
    # t0_normalize, t1_normalize = gradient_descent(Xn, Yn, initial_t0, initial_t1, learning_rate, num_iterations)
    # t0, t1 = denormalize(X, Y, t0_normalize, t1_normalize)

    # print("t0 = {0}".format(t0_normalize))
    # print("t1 = {0}".format(t1_normalize))
    # showVisu(Xn, Yn, t0_normalize, t1_normalize)
    # showVisu(X, Y, t0, t1)
    # return (t0, t1)