from __future__ import division
from itertools import tee, cycle
import math
from numpy.ma import arange
from Drawer import add_to_plot, draw_plot

__author__ = 'wiktor'
from FunctionValuesCalculator import calculate_f_x_1, calculate_differential_equation

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


def solve_with_euler_method(k, m, x0, xk, n, h, t, w, x):
    for i in range(0, n):
        w.append(w[i] + h * calculate_differential_equation(t, w[i], k, m))
        t += h
        x.append(t)

def solve_with_runge_kutta_method(k, m, x0, xk, n, h, t, w, x):
    for i in range(0, n):
        k1 = calculate_differential_equation(t, w[i], k, m)
        k2 = calculate_differential_equation(t + h/2, w[i] + k1 * h/2, k, m)
        k3 = calculate_differential_equation(t + h/2, w[i] + k2 * h/2, k, m)
        k4 = calculate_differential_equation(t + h, w[i] + h*k3, k, m)
        w.append(w[i] + h*(k1 + 2*k2 + 2*k3 + k4)/6)
        t += h
        x.append(t)

def solve_equation(k, m, x0, xk, n, h, t, w, x, solver, method_name, draw_flag):
    solver(k, m, x0, xk, n, h, t, w, x)
    xx = arange(x0, xk, 0.1)
    f_y = []
    for i in x:
        f_y.append(calculate_f_x_1(i, k, m))
    mean_square_error = calculate_mean_square_error(x,f_y, w)
    max_error = calculate_max_norm(x, f_y, w)
    mean_format = "{:.4f}"
    max_format = "{:.4f}"
    if mean_square_error < 0.0001:
        mean_format = "{:.3e}"
    elif mean_square_error > 100:
        mean_format = "{:.0f}"
    if max_error < 0.0001:
        max_format = "{:.3e}"
    elif max_error > 100:
        max_format = "{:.0f}"
    print(";".join((str(n),mean_format.format(mean_square_error), max_format.format(max_error))))
    if draw_flag:
        add_to_plot(xx, calculate_f_x_1(xx, k, m), "Given function")
        add_to_plot(x, w, method_name +  " differential")
        file_name = method_name + "_"+str(n)
        title = method_name + "  n = "+str(n)+"\n mean square error = " + mean_format.format(mean_square_error) + "\n max error = " + max_format.format(max_error)
        draw_plot(title, file_name)


def go():
    k = 4
    m = 2
    x0 = -math.pi/4
    xk = 3 * math.pi/2
    n = 100000
    print("n;mean square error; max error")
    i = 1
    step = 1
    while i <= n:
        if i < 10:
            step = 1
        elif 10 <= i < 100:
            step = 10
        elif 100 <= i < 2000:
            step = 100
        elif 2000 <= i < 20000:
            step = 1000
        else:
            step = 10000
        h = (xk - x0)/i
        t = x0
        a = calculate_f_x_1(x0, k, m)
        w = [float(a)]
        x = [float(t)]
        draw_flag = True
        solve_equation(k, m, x0, xk, i, h, t, w, x, solve_with_euler_method, "Euler", draw_flag)
        # solve_equation(k, m, x0, xk, i, h, t, w, x, solve_with_runge_kutta_method, "Runge-Kutta", draw_flag)
        i += step



go()