from numpy.linalg import linalg
from numpy.numarray import zeros

__author__ = 'Wiktor'
import numpy as np


def calculate_quadratic_value(t, y):
    n = len(t)
    z = [0]

    for i in range(0, n - 1):
        z.append(-z[i] + 2 * ((y[i + 1] - y[i]) / (t[i + 1] - t[i])))
    return z


def calculate_quadratic_value_not_a_knot(t, y):
    n = len(t)
    d = [(y[1] - y[0]) / (t[1] - t[0])]
    A = zeros(shape=(n, n))
    A[0][0] = 1

    for i in range(1, n):
        A[i][i-1] = 1
        A[i][i] = 1
        d.append(2 * ((y[i] - y[i-1]) / (t[i] - t[i-1])))

    return linalg.solve(A, d)



def create_quadratic_function(t, y, calc):
    z = calc(t, y)

    def foo(x):
        i = 0
        while x - t[i] >= 0:
            i += 1
        i -= 1
        return ((z[i + 1] - z[i]) * (x - t[i]) * (x - t[i])) / (2 * (t[i + 1] - t[i])) + z[i] * (x - t[i]) + y[i]

    return foo


def calculate_cubic_value(t, y):
    n = len(t)
    h = []
    b = []
    u = [0]
    v = [0]

    for i in range(0, n - 1):
        h.append(t[i + 1] - t[i])
        b.append(6 * (y[i + 1] - y[i]) / h[i])

    u.append(2 * (h[0] + h[1]))
    v.append(b[1] - b[0])

    for i in range(2, n - 1):
        u.append(2 * (h[i - 1] + h[i]) - (h[i - 1] * h[i - 1]) / u[i - 1])
        v.append((b[i] - b[i - 1]) - (h[i - 1] * v[i - 1] / u[i - 1]))

    z = [0] * (n)
    for i in range(n - 2, 0, -1):
        z[i] = ((v[i] - h[i] * z[i + 1]) / u[i])
        # print "n: " + str(i) + "z[i]: " + str(z[i])
    z[0] = 0
    return z, h


def id(x):
    return x


def calculate_cubic_value_not_a_knot(t, y):
    n = len(t)
    h = []
    b = []
    v = [0]
    A = zeros(shape=(n, n))

    for i in range(0, n - 1):
        h.append(t[i + 1] - t[i])
        b.append(6 * (y[i + 1] - y[i]) / h[i])

    A[0][0] = h[1]
    A[0][1] = - h[1] - h[0]
    A[0][2] = h[0]

    for i in range(1, n - 1):
        A[i][i - 1] = h[i - 1]
        A[i][i] = 2 * (h[i - 1] + h[i])
        A[i][i + 1] = h[i]
        v.append(b[i] - b[i - 1])
    v.append(0)
    A[n - 1][n - 3] = h[n - 2]
    A[n - 1][n - 2] = - h[n - 2] - h[n - 3]
    A[n - 1][n - 1] = h[n - 3]

    z = linalg.solve(A, v)

    return z, h


def create_spline_function(t, y, calc):
    z, h = calc(t, y)

    def foo(x):
        i = 0
        while float(x) - t[i] >= 0:
            i += 1
        i -= 1
        A = (z[i + 1] - z[i]) / (6 * h[i])
        B = z[i] / 2.
        C = -(h[i] * (z[i + 1] + 2 * z[i])) / 6 + (y[i + 1] - y[i]) / h[i]
        return y[i] + ((x - t[i]) * (C + (x - t[i]) * (B + (x - t[i]) * A)))

    return foo