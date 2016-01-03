from math import pi
import math
from numpy import arange, linspace
from FunctionValuesCalculator import calculate_f_x
from SplineFunctionsCreator import create_spline_function, calculate_quadratic_value, calculate_cubic_value_not_a_knot, \
    calculate_cubic_value, calculate_quadratic_value_not_a_knot, create_quadratic_function
import matplotlib.pyplot as plt
import scipy.interpolate as sci

__author__ = 'Wiktor'

N = 100
start = -2. * pi
end = 2. * pi


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


# def drawer(x, fi, fy, label, n):


def interpolate(n):
    points = get_points(n - 1)
    points = map(list, zip(*points))
    a, b = points
    t = points[0]
    y = points[1]
    cubic_spline_natural = create_spline_function(t, y, calculate_cubic_value)
    cubic_spline_not_a_knot = create_spline_function(t, y, calculate_cubic_value_not_a_knot)
    quadratic_spline_natural = create_quadratic_function(t, y, calculate_quadratic_value)
    quadratic_spline_not_a_knot = create_quadratic_function(t, y, calculate_quadratic_value_not_a_knot)
    x = arange(-2 * pi, 2 * pi, 0.05)
    w = map(cubic_spline_natural, x)
    w1 = map(quadratic_spline_natural, x)
    w2 = map(cubic_spline_not_a_knot, x)
    w3 = map(quadratic_spline_not_a_knot, x)
    plt.plot(x, calculate_f_x(x), 'b', linewidth=2.5, label="given f")
    plt.plot(x, w, 'r--', linewidth=2.5, label="interpolated cubic")
    # plt.plot(x + 0.2, w2, 'g--', linewidth=2.5, label="interpolated cubic")
    plt.plot(a, b, 'yo')
    # plt.plot(x, [cubicSpline(a) for a in x], 'r--', linewidth=2.5, label="interpolated cubic")
    plt.plot(x, w1, 'c--', linewidth=2.5, label="interpolated quadratic")
    plt.plot(x, w3, 'm--', linewidth=2.5, label="interpolated quadratic")
    # f = sci.interp1d(a, b, kind="cubic")
    # plt.plot(x, f(x), '--', label='interpolated test')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()


def interpolate2(n, spline_creator, boundary_conditions, label=0, caption=0):
    points = get_points(n - 1)
    points = map(list, zip(*points))
    t = points[0]
    y = points[1]
    spline = spline_creator(t, y, boundary_conditions)
    x = arange(-2 * pi, 2 * pi, 0.05)
    f_i = map(spline, x)
    f_y = map(calculate_f_x, x)
    if caption != 0:
        plt.figure(num=1, figsize=(10, 6), dpi = 150)
        plt.plot(x, calculate_f_x(x), 'b--', linewidth=1, label="given f")
        plt.plot(x, f_i, 'r--', linewidth=1, label=label)
        plt.plot(t, y, 'yo', label="Nodes: " + str(n))
        plt.legend(loc='upper left', prop={'size':8})
        plt.grid(True)
        # plt.savefig(str(n) + "_" + caption + ".png", dpi=150)
        # plt.show()
        plt.close()
    print ";" + str("{:1.7f}".format(calculate_mean_square_error(x, f_y, f_i))),


# interpolate(30)


def launcher(spline_creator, boundary_conditions, label, caption=0):
    n = 4
    print ";4;8;16;32;64;128"
    print label,
    while n <= 128:
        interpolate2(20, spline_creator, boundary_conditions, label, caption)
        n *= 2
    print


def go():
    launcher(create_spline_function, calculate_cubic_value, "cubic spline - natural conditions", "cubic_natural")
    launcher(create_spline_function, calculate_cubic_value_not_a_knot, "cubic spline - not-a-knot conditions", "cubic_knot")
    launcher(create_quadratic_function, calculate_quadratic_value, "quadratic spline - natural conditions", "quadratic_natural")
    launcher(create_quadratic_function, calculate_quadratic_value_not_a_knot,
             "quadratic spline - not-a-knot conditions", "quadratic_zero")


go()