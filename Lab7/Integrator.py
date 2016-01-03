from math import pi, cos
from FunctionValuesCalculator import calculate_f_x
from scipy import *
import scipy.special as sp
import matplotlib.pyplot as plt

__author__ = 'Wiktor'

start = -2. * pi
end = 2. * pi
real_val = 48.7675

def newton_cotes_integrate(points, M, a, b):
    x_vector, y_vector = zip(*points)
    result = 0
    n = len(x_vector)
    step = (b - a) / (n - 1)
    if M == 1:
        for i in range(1, n):
            result += (step / 2) * (y_vector[i - 1] + y_vector[i])

    elif M == 2:
        for i in range(2, n, 2):
            result += (step / 3) * (y_vector[i - 2] + 4 * y_vector[i - 1] + y_vector[i])

    elif M == 3:
        for i in range(3, n, 3):
            result += ((3 * step) / 8) * (y_vector[i - 3] + 3 * y_vector[i - 2] + 3 * y_vector[i - 1] + y_vector[i])
    return result


def gauss_legendre_integrate(n, a, b):
    [Ws, xs, err] = GaussLegendreWeights(n)
    half_lenght = (b - a) / 2.
    # print half_lenght
    if err == 0:
        ans = half_lenght * sum(Ws * calculate_f_x(half_lenght * xs + (b + a) * 0.5))
    else:
        err = 1
        ans = None
    return [ans, err]


def get_points(n, a, b):
    points = []
    r = b - a
    step = r / n
    for i in arange(-2 * pi, 2 * pi, step):
        points.append((i, calculate_f_x(i)))
    points.append((b, calculate_f_x(b)))
    return points



def Legendre(n, x):
    x = array(x)
    if (n == 0):
        return x * 0 + 1.0
    elif (n == 1):
        return x
    else:
        return ((2.0 * n - 1.0) * x * Legendre(n - 1, x) - (n - 1) * Legendre(n - 2, x)) / n


def DLegendre(n, x):
    x = array(x)
    if (n == 0):
        return x * 0
    elif (n == 1):
        return x * 0 + 1.0
    else:
        return (n / (x ** 2 - 1.0)) * (x * Legendre(n, x) - Legendre(n - 1, x))


def GaussLegendreWeights(polyorder):
    W = []
    xis = array(sp.legendre(polyorder).r)
    # [xis, err] = LegendreRoots(polyorder)
    # print xis
    err = 0
    for i in range(0, polyorder):
        if isinstance(xis[i], complex):
            err = 1
    if err == 0:
        W = 2.0 / ( (1.0 - xis ** 2) * (DLegendre(polyorder, xis) ** 2) )
        err = 0
    else:
        err = 1  # could not determine roots - so no weights
    return [W, xis, err]


def integrate(n, M):
    # points = get_points(n)
    print str(M) + ";" + str(M*2) + ";" + str(n),
    # newton_result = newton_cotes_integrate(points, M)

    length = end - start
    subinterval_lenght = abs(length/n)
    a = start
    b = start + subinterval_lenght
    sum = 0
    newton_result = 0
    while b <= end:
        [res, err] = gauss_legendre_integrate(2*M, a, b)
        points = get_points(M, a, b)
        tmp = newton_cotes_integrate(points, M, a, b)
        newton_result += tmp
        sum += res
        a += subinterval_lenght
        b += subinterval_lenght
    # print sum
    # [res, _] = gauss_legendre_integrate(n, start, end)
    print ";" + str(newton_result) + ";" + str("{:1.4f}".format(abs((newton_result - real_val)/real_val))),
    print ";" + str(sum) + ";" + str("{:1.4f}".format(abs((sum - real_val)/real_val)))
    return n, "{:1.4f}".format(abs((newton_result - real_val)/real_val) * 100), "{:1.4f}".format(abs((sum - real_val)/real_val) * 100)

# integrate(21, 3)


def go():
    print "nodes newton;nodes gauss;subintervals;newton;newton error;gauss;gauss error"
    tu = []
    for i in range(1, 4):
        for j in range(2, 30):
            tu.append(integrate(j, i))
    n = []
    bg = []
    bn = []
    print tu
    for i in range(0, len(tu)):
        a,b,c = tu[i]
        n.append(a)
        bn.append(float(b))
        bg.append(float(c))
    plt.plot(n, bn, 'yo', label = "newton error")
    plt.plot(n, bg, 'go', label = "gauss error")
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

go()