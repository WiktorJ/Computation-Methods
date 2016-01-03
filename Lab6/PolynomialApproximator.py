from numpy.linalg import linalg

__author__ = 'Wiktor'


def fill_s_matrix(x_vector, m):
    matrix = []
    for i in range(0, m+1):
        i_row = []
        for j in range(0, m+1):
            i_row.append(reduce(lambda sum, x: sum + pow(x, i + j), x_vector, 0))
        matrix.append(i_row)
    return matrix


def fill_y_vector(x_vector, y_vector, m):
    vector = []
    for i in range(0, m+1):
        vector.append(reduce(lambda sum, (x, y): sum + y * pow(x, i), zip(x_vector, y_vector), 0))
    return vector


def approximate(points, m):
    x_vector, y_vector = zip(*points)
    S = fill_s_matrix(x_vector, m)
    Y = fill_y_vector(x_vector, y_vector, m)
    A = linalg.solve(S, Y)

    def foo(x_point):
        result = 0
        for i in range(0, m+1):
            result += pow(x_point, i) * A[i]
        return result
    return foo
