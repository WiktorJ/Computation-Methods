__author__ = 'Wiktor'
from math import pi, cos
from numpy import arange
from FunctionValuesCalculator import *
import PolynomialApproximator as pa
import TrigonometricApproximator as ta
import matplotlib.pyplot as plt

N = 100
start = -2. * pi
end = 2. * pi
font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 12,
        }

def get_chebyshev_points(n):
    points = []

    half_length = (end - start) / 2
    middle = start + half_length

    for i in range(0, n):
        x = middle + cos(((2 * i + 1) * pi) / (2 * n)) * half_length
        y = calculate_f_x(x)
        points.append((x, y))
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


def calculate_max_norm(x, f_y, f_i):
    result = 0;
    for i in range(0, len(f_y)):
        result = max(abs(f_y[i] - f_i[i]), result)
    return result


def approximate(n, m):
    points = get_points(n)
    polynomial_approximated_function = pa.approximate(points, m)
    trigonometric_approximated_function = ta.approximate(points, m)
    x = arange(-2 * pi, 2 * pi, 0.05)
    f_y = map(calculate_f_x, x)
    polynomial_y = map(polynomial_approximated_function, x)
    trigonometric_y = map(trigonometric_approximated_function, x)
    x_list = []
    y_list = []
    for x_p, y_p in points:
        x_list.append(x_p)
        y_list.append(y_p)
    p_max_norm = calculate_max_norm(x, f_y, polynomial_y)
    p_euclidean_norm = calculate_mean_square_error(x, f_y, polynomial_y)
    t_max_norm = calculate_max_norm(x, f_y, trigonometric_y)
    t_euclidean_norm = calculate_mean_square_error(x, f_y, trigonometric_y)
    if t_euclidean_norm > 0.0001:
        print ";" + "{:.4f}".format(t_euclidean_norm),
    else:
        print ";" + "{:.3e}".format(t_euclidean_norm),
    plt.plot(x, calculate_f_x(x), "r--", linewidth=0.5, label="given f")
    plt.plot(x, polynomial_y, 'g--', linewidth=0.5, label="polynomial approximated f")
    plt.plot(x, trigonometric_y, 'b--', linewidth=0.5, label="trigonometric approximated f")
    if n < 50: plt.plot(x_list, y_list, 'yo')
    plt.title("nodes: " + str(n) + "  degree: " + str(m) + "\n  polynomial: max error: " + "{:.3f}".format(
        p_max_norm) + " | mean square error: " + "{:.3f}".format(
        p_euclidean_norm) + "\n  trigonometric: max error: " + "{:.3f}".format(t_max_norm) + " | mean square error: " + "{:.3f}".format(t_euclidean_norm), fontdict=font)
    plt.figure(num=1, figsize=(10, 6), dpi=150)
    plt.legend(loc='upper left', prop={'size': 8})
    plt.grid(True)
    # plt.savefig("charts/" + "points_" + str(n) + "_degree_" + str(m) + '.png')
    # plt.show()
    plt.close()
    return (p_max_norm, t_max_norm, n, m)


def go():
    i = 2
    print ";2;4;8;16;32"
    j = 10
    g = []
    while j <= 1000:
        l = []
        print str(j),
        while i <= 64 and i < j:
            tmp = approximate(j, i)
            l.append(tmp)
            g.append(tmp)
            i *= 2
        i = 2
        if j < 50:
            step = 5
        elif 50 <= j < 100:
            step = 10
        else:
            step = 100
        j += step
        print
        # p_m, t_m, n, m = map(list, zip(*l))
        # plt.plot(m, p_m, "b--")
        # plt.show()
        # plt.close()
    # g = sorted(g, key=lambda tup: tup[3])
    p_m, t_m, n, m = map(list, zip(*g))
    # wr = []
    # pr = []
    # for i in xrange(0, len(g)):
    #     (p_m,_,c,d) = g[i]
    #     print g[i]
        # if d== 8 :
        #     wr.append(p_m)
        #     pr.append(c)
    #
    # plt.plot(wr, pr, "b--")
    # plt.show()
    # plt.close()
    #
    # print g

# approximate(40,20)
go()