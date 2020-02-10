
def gradient_descent_runner(points,starting_t0, starting_t1, learning_rate, num_iterations):
    t0 = starting_t0
    t1 = starting_t1
    cpt = 0
    
    for i in range(num_iterations):
        t0_gradient = 0 # somme derive par rapport à t0
        t1_gradient = 0 # somme derive par rapport à t1
        N = float(len(points))
        for j in range(0, len(points)):
            x = points[j][0]
            y = points[j][1]
            t0_gradient +=  (-2 * (y - (t0 + t1 * x)))
            t1_gradient += (-2 * x * (y - (t0 + t1 * x)))
        step_size_intercept = learning_rate * t0_gradient
        step_size_slope = learning_rate * t1_gradient
        t0 =  t0 - learning_rate * t0_gradient
        t1 =  t1 - learning_rate * t1_gradient
        print("Step size 0= {0}".format(step_size_intercept))
        print("Step size 1 = {0}".format(step_size_slope))
        cpt += 1
        if abs(learning_rate * t0_gradient) <= 0.001 and abs(learning_rate * t1_gradient) <= 0.001 :
            print(cpt)
            return[t0, t1]
    print("yo")
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

    learning_rate = 0.001
    #y = t0 + t1x (slope formula)
    initial_t0 = 0
    initial_t1 = 0
    num_iterations = 1500
    print(points)
    [t0, t1] = gradient_descent_runner(points, initial_t0, initial_t1, learning_rate, num_iterations)
    #return to predict.py theta0, theta1, visu
           
    return (t0, t1, visu)