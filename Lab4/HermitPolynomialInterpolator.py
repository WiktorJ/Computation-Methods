import numpy
from FunctionValuesCalculator import calculate_f_p_x
from numpy.polynomial.hermite import hermval

__author__ = 'Wiktor'


# points = [(input[0][0], input[0][1] - 0), (input[0][0], calculate_f_p_x(input[0][0]))] #"input[0][1] - 0" this is just to change type of second element
# calculate_f_p_x
# returns
# value
# of
# derivative
# for k in range(1, len(input)): #Divided differences and derivatives in one list alternately
# points.append((input[k][0], (input[k][1] - input[k - 1][1]) / (
# input[k][0] - input[k - 1][0])))
# points.append((input[k][0], calculate_f_p_x(input[k][0])))
# x, c = zip(*points)
# x = list(x)
# c = list(c)
# n = len(points)
# for i in range(2, n): #calculating factors
# for j in range(n - 1, i - 1, -1):
# c[j] = (c[j] - c[j - 1]) / (x[j] - x[j - i])
def hermit_interpolate(input):  #input is list of tuples [(x1,y1),(x2,y2),...,(xn,yn)] xi are Chebyshev nodes
    n = len(input)
    points = numpy.zeros(shape=(2 * n + 1, 2 * n + 1))
    X, Y = zip(*input)
    X = list(X)
    Y = list(Y)

    for i in range(0, 2 * n, 2):
        points[i][0] = X[i / 2]
        points[i + 1][0] = X[i / 2]
        points[i][1] = Y[i / 2]
        points[i + 1][1] = Y[i / 2]

    for i in range(2, 2 * n + 1):
        for j in range(1 + (i - 2), 2 * n):
            if i == 2   and j % 2 == 1:
                points[j][i] = calculate_f_p_x(X[j / 2]);

            else:
                points[j][i] = (points[j][i - 1] - points[j - 1][i - 1]) / (
                    points[j][0] - points[(j - 1) - (i - 2)][0])

    def result_polynomial(xpoint):  #here is function to calculate value for given x
        val = 0
        for i in range(0, 2 * n):
            factor = 1.
            j = 0
            while j < i:
                factor *= (xpoint - X[j / 2])
                if j + 1 != i:
                    factor *= (xpoint - X[j / 2])
                    j += 1
                j += 1
            val += factor * points[i][i + 1]
        return val

        # val = c[0]
        # factor = 1.0
        # for l in range(1, n):
        #     factor *= (xpoint - x[l - 1])
        #     val += (c[l] * factor)
        # return val

    return result_polynomial