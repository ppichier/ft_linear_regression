

def step_gradient(t0_current, t1_current, points, learning_rate):
    t0_gradient = 0 # somme derive par rapport à t0
    t1_gradient = 0 # somme derive par rapport à t1
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i][0]
        y = points[i][1]
        t0_gradient += ((t0_current + t1_current * x) - y )
        t1_gradient += (x * ((t0_current + t1_current * x) - y))
    new_t0 =  learning_rate * t0_gradient * (1/N)
    new_t1 =  learning_rate * t1_gradient * (1/N)
    # print("theta0  = {0}".format(new_t0))
    # print("theta1  = {0}".format(new_t1))
    return [new_t0, new_t1]


def gradient_descent_runner(points,starting_t0, starting_t1, learning_rate, num_iterations):
    t0 = starting_t0
    t1 = starting_t1
    
    for i in range(num_iterations):
        print("t0 = {0}".format(t0))
        print("t1 = {0}".format(t1))
        t0, t1 = step_gradient(t0, t1, points, learning_rate)
    return [t0,t1]


def train():
    try:
        with open('data2.csv', 'r') as f:
            points = [] # points [ [x1, y1], ... , [xn, yn] ]
            visu = [ [],[] ] #list of x and y coordinates for visu [ [x1,...,xn] , [y1,...,yn] ]
            for i in range(1):
                f.readline()
            for line in f:
                line = line.rstrip()
                words = line.split(',')
                visu[0].append(float(words[0]))
                visu[1].append(float(words[1]))
                points.append([ float(words[0]),float(words[1]) ])
    except Exception as e:
        raise Exception(e)

    learning_rate = 0.0001
    #y = t0 + t1x (slope formula)
    initial_t0 = 0
    initial_t1 = 0
    num_iterations = 50
    print(points)
    [t0, t1] = gradient_descent_runner(points, initial_t0, initial_t1, learning_rate, num_iterations)
    #return to predict.py theta0, theta1, visu
           
    return (t0, t1, visu)