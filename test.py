

## Gradient descent Method for calculate the intercept only
# 1) use the sum of the squared residuals as the Loss function to evaluate how a line fits the data
# 2) take the derivative of the sum of the squared residuals ( we took the derivative of the loss function)
# 3) Then we calculated the derivative when the Intercept = 0 (random value)
# 4) Plug that slope into the Step Size calculation : Step Size = Slope * Learning rate
# 5) Calculated the new intercept , the difference between the old intercept and the Step size 
# 6) Lastly, we plugged the New Intercept into derivative and repeated everything until Step size was close to 

## Gradient descent Method for calculate the intercept and the slope: y = tetha0 + theta1 * x
## where theta0 is the intercept and theta1 the slope
# 1) We want to find the values for the intercept and slope that give us the minimum sum of the squared residuals
# 2) take the derivative of the sum of the squared residuals ( we took the derivative of the loss function)
# - this time we take the derivative with respect to the intercept AND the derivtive with respect to the slope
# - d / d intercept AND d / d slope
# 4) Derivative with repect of the intercept -> The chain rule
from numpy import * 

def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) **2
    return totalError / float(len(points))

def step_gradient(b_current, m_current, points, learning_rate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current)) # squared residuals sums in b_gradient for intercept
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))# squared residuals sums in m_gradient for the slope
    new_b = b_current - (learning_rate * b_gradient) # new Intercept = b_current - StepSize intercept
    new_m = m_current - (learning_rate * m_gradient) # new Slope = b_current - StepSize slope
    return [new_b, new_m]

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m

    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]

def run():
    points = genfromtxt('data.csv', delimiter=",")
    #hyperparameters (How fast our model run)
    learning_rate = 0.0001
    #y = mx + b (slope formula)
    initial_b = 0
    initial_m = 0
    num_iterations = 1000
    print ("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points)))
    print ("Running...")
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print ("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points)))


if __name__ == '__main__':
    run()