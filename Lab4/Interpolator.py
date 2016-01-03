from math import pi, cos
from numpy import arange
from HermitPolynomialInterpolator import hermit_interpolate

__author__ = 'Wiktor'
from FunctionValuesCalculator import *
from LagrangePolynomialInterpolator import *
from NewtonPolynomialInterpolator import *
import matplotlib.pyplot as plt

N = 100
start = -2. * pi
end = 2. * pi


def get_chebyshev_points(n):
    points = []

    half_length = (end - start) / 2
    middle = start + half_length

    for i in range(0, n):
        x = middle + cos(((2 * i + 1) * pi) / (2 * n)) * half_length
        y = calculate_f_x(x)
        points.append((x, y))
    # for i in range(0, n):
    # p = cos((2. * i + 1.)*pi/(2. * n)*pi)
    # points.append(p)
    # r2 = end - start
    # for i in range(0, n):
    #     points[i] = points[i]/2. + 0.5
    #     points[i] = (points[i] * r2) + start
    # points2 = [(end, calculate_f_x(end))]
    # print points
    #     points2 = []
    # print points2
    # for i in range(1, n):
    #     points2.append((points[i], calculate_f_x(points[i])))
    # points2.append((start, calculate_f_x(start)))
    #     print points2
    return points


def get_points(n):
    points = []
    r = end - start
    step = r / n
    for i in arange(-2 * pi, 2 * pi, step):
        points.append((i, calculate_f_x(i)))
    points.append((end, calculate_f_x(end)))
    return points


def calculate_mean_square_error(x, f_y, f_i):
    n = len(x)
    mean_squared_error = 0
    for i in range(0, n):
        mean_squared_error += math.pow(f_y[i] - f_i[i], 2)
    mean_squared_error /= n
    return mean_squared_error


def calculate_max_error(x, f_y, f_i):
    n = len(x)
    max_error = 0
    for i in range(0, n):
        if math.fabs(f_y[i] - f_i[i]) > max_error:
            max_error = math.fabs(f_y[i] - f_i[i])
    return max_error


def interpolate(n):
    # points = get_points(n)
    points = get_chebyshev_points(n)
    lagrange_polynomial = lagrange_interpolate(points)
    newton_polynomial = newton_interpolate(points)
    hermit_polynomial = hermit_interpolate(points)
    x = arange(-2 * pi, 2 * pi, 0.1)
    f_y = map(calculate_f_x, x)
    lagrange_y = map(lagrange_polynomial, x)
    newton_y = map(newton_polynomial, x)
    hermit_y = map(hermit_polynomial, x)
    x_list = []
    y_list = []
    for x_p, y_p in points:
        x_list.append(x_p)
        y_list.append(y_p)
    print "nodes;Lagrange;Newton;Hermite;Lagrange;Newton;Hermite"
    print ";".join((
        str(n), str("{:1.5f}".format(calculate_mean_square_error(x, f_y, lagrange_y))), str("{:1.5f}".format(calculate_mean_square_error(x, f_y, newton_y))),
        str("{:1.5f}".format(calculate_mean_square_error(x, f_y, hermit_y))), str("{:1.5f}".format(calculate_max_error(x, f_y, lagrange_y))),
        str("{:1.5f}".format(calculate_max_error(x, f_y, newton_y))), str("{:1.5f}".format(calculate_max_error(x, f_y, hermit_y)))))
    plt.plot(x, calculate_f_x(x), "r--", linewidth=2.5, label="given f")
    plt.plot(x, lagrange_y, 'g--', linewidth=2.5, label="interpolated lagrange f")
    # plt.plot((x + 0.3), lagrange_y, 'g--', linewidth=2.5, label="interpolated lagrange f")
    plt.plot(x, newton_y, 'b--', linewidth=2.5, label="interpolated newton f")
    # plt.plot((x + 0.6), newton_y, 'b--', linewidth=2.5, label="interpolated newton f")
    if n < 30:
        plt.plot(x, hermit_y, 'c--', linewidth=2.5, label="interpolated hermit f")
        # plt.plot((x + 0.9), hermit_y, 'c--', linewidth=2.5, label="interpolated hermit f")
    plt.plot(x_list, y_list, 'yo')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()


# def go():
#     for i in range(5, 55, 5):
#         interpolate(i)
#
# go()
interpolate(20)