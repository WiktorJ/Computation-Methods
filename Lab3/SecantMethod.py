__author__ = 'Wiktor'
from FunctionValuesCalculator import *


def calculate_root_secant(starting_point_a, starting_point_b, stop_condition_x_diff, stop_condition_f_val, max_iteration, n, m):
    x0 = starting_point_a
    x1 = starting_point_b
    f0 = calculate_f_x(x0, n, m)
    f1 = calculate_f_x(x1, n, m)
    i = 0

    while (i < max_iteration) and (abs(x1 - x0) > stop_condition_x_diff):
        x2 = x1 - (f1*(x1 - x0))/(f1 - f0)
        x0 = x1
        x1 = x2
        f0 = f1
        f1 = calculate_f_x(x1, n, m)
        i += 1

    roots = (x1, i)
    x0 = starting_point_a
    x1 = starting_point_b
    f0 = calculate_f_x(x0, n, m)
    f1 = calculate_f_x(x1, n, m)
    i = 0

    while (i < max_iteration) and (abs(calculate_f_x(x0, n, m)) > stop_condition_f_val):
        x2 = x1 - (f1*(x1 - x0))/(f1 - f0)
        x0 = x1
        x1 = x2
        f0 = f1
        f1 = calculate_f_x(x1, n, m)
        i += 1

    roots = roots + (x1, i)
    return roots