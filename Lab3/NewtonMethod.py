__author__ = 'Wiktor'
from FunctionValuesCalculator import *


def calculate_root_newton(starting_point, stop_condition_x_diff, stop_condition_f_val, max_iteration, n, m):
    x1 = starting_point + 1
    x0 = starting_point
    i = 0
    while (i < max_iteration) and (abs(x1 - x0) > stop_condition_x_diff):
        x1 = x0
        f1 = calculate_f_p_x(x0, n, m)
        f0 = calculate_f_x(x0, n, m)
        x0 -= f0 / f1
        i += 1

    roots = (x0, i)
    x0 = starting_point
    i = 0
    while (i < max_iteration) and (abs(calculate_f_x(x0, n, m)) > stop_condition_f_val):
        f1 = calculate_f_p_x(x0, n, m)
        f0 = calculate_f_x(x0, n, m)
        x0 -= f0 / f1
        i += 1
    roots = roots + (x0, i)
    return roots