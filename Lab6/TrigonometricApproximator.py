from math import sin, cos, pi
from numpy.linalg import linalg
import math

__author__ = 'Wiktor'


end = 2. * pi
start = -2. * pi


def polynomial(x, i):
    # half_length = (end - start) / 2
    if i == 0:
        return 1
    if i % 2 == 0:
        return cos(x * i / 2) #* half_length
    else:
        return sin(x * (i + 1) / 2)# * half_length


def fill_s_matrix(x_vector, m):
    matrix = []
    for i in range(0, m + 1):
        i_row = []
        for j in range(0, m + 1):
            sum = 0
            for k in range(0, len(x_vector)):
                sum += polynomial(x_vector[k], j) * polynomial(x_vector[k], i)
            i_row.append(sum)
        matrix.append(i_row)
    return matrix


def fill_y_vector(x_vector, y_vector, m):
    vector = []
    for i in range(0, m + 1):
        sum = 0
        for k in range(len(x_vector)):
            sum += polynomial(x_vector[k], i) * y_vector[k]
        vector.append(sum)
    return vector


def approximate(points, m):
    x_vector, y_vector = zip(*points)
    S = fill_s_matrix(x_vector, m)
    Y = fill_y_vector(x_vector, y_vector, m)
    A = linalg.solve(S, Y)


    def foo(x_point):
        result = 0
        for i in range(0, m + 1):
            result += polynomial(x_point, i) * A[i]
        return result

    return foo