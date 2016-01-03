import time

__author__ = 'Wiktor'
from NewtonMethod import *
from SecantMethod import *
import matplotlib.pyplot as plt
import numpy as np


def calculate_roots(a, b, p):
    n = 15
    m = 15
    border_a = a
    border_b = b
    iteration_cond = a
    iteration_cond2 = b
    max_iteration = 10000
    t1 = np.arange(a - 1, b + 1, 0.1)
    plt.plot(t1, calculate_f_x(t1, n, m), 'b-')
    plt.grid(True)
    while border_b > iteration_cond:
        (x1, i1, x2, i2) = calculate_root_newton(a, p, p, max_iteration, n, m)
        (y1, j1, y2, j2) = calculate_root_secant(a, border_b, p, p, max_iteration, n, m)
        (z1, k1, z2, k2) = calculate_root_secant(border_a, b, p, p, max_iteration, n, m)
        plt.setp(plt.plot(x1, calculate_f_x(x1, n, m), 'bo'), color='r')
        (a1, b1, p1) = (border_a, border_b, p)
        print(";".join((
        str(x1), str(i1), str(x2), str(i2), str(y1), str(j1), str(y2), str(j2), str(z1), str(k1), str(z2), str(k2),
        str(round(a1, 2)), str(round(b1, 2)), str(p1))))
        border_b -= 0.1
        border_a -= 0.1

    while border_a < iteration_cond2:
        (x1, i1, x2, i2) = calculate_root_newton(a, p, p, max_iteration, n, m)
        (y1, j1, y2, j2) = calculate_root_secant(a, border_b, p, p, max_iteration, n, m)
        (z1, k1, z2, k2) = calculate_root_secant(border_a, b, p, p, max_iteration, n, m)
        plt.setp(plt.plot(x1, calculate_f_x(x1, n, m), 'bo'), color='r')
        (a1, b1, p1) = (border_a, border_b, p)
        print(";".join((
        str(x1), str(i1), str(x2), str(i2), str(y1), str(j1), str(y2), str(j2), str(z1), str(k1), str(z2), str(k2),
        str(round(a1, 2)), str(round(b1, 2)), str(p1))))
        border_b += 0.1
        border_a += 0.1

    plt.show()


def start():
    print("NM root1;NM iterations1;NM root2;NM iterations2;"
          " SM root1_a;SM iterations1_a;SM root2_a;SM iterations2_a;"
          " SM root1_a;SM iterations1_a;SM root2_a;SM iterations2_a;border a;border b;accuracy)")
    for i in range(6, 9):
        for j in np.arange(-2, 1, 0.5):
            calculate_roots(-1. + j, 0.6 + j, pow(10, -2 * i))


start()

