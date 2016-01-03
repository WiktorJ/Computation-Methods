from numpy.linalg import inv

__author__ = 'Wiktor'
from FunctionValuesCalculator import *
import numpy as np


def calculate_root_newton(vector, stop_condition_x_diff, stop_condition_f_val, max_iteration):
    shape = (3, 3)
    x11 = [x + 1 for x in vector]
    x00 = vector
    x1 = np.array(x11)
    x0 = np.array(x00)
    i = 0
    while (i < max_iteration) and ((abs(x1[0] - x0[0]) > stop_condition_x_diff) or (abs(x1[1] - x0[1]) > stop_condition_x_diff) or (abs(x1[2] - x0[2]) > stop_condition_x_diff)):
        x1 = np.copy(x0)
        J0 = [[calculate_f1_x1(x0[0]), calculate_f1_x2(x0[1]), calculate_f1_x3(x0[2])],
             [calculate_f2_x1(x0[0]), calculate_f2_x2(x0[2]), calculate_f2_x3(x0[2])],
             [calculate_f3_x1(x0[0]), calculate_f3_x2(x0[1]), calculate_f3_x3(x0[2])]]
        f00 = [calculate_f1(x0[0], x0[1], x0[2]), calculate_f2(x0[0], x0[1], x0[2]), calculate_f3(x0[0], x0[1], x0[2])]
        J = np.array(J0)
        f0 = np.array(f00)
        J.reshape(shape)
        try:
            invJ = inv(J)
            x0 -= np.dot(invJ, f0)
        except np.linalg.linalg.LinAlgError:
            x0 = "Singular_matrix"
            break
        i += 1
    roots = (x0, i)
    x0 = vector
    i = 0
    while (i < max_iteration) and ((abs(calculate_f1(x0[0], x0[1], x0[2])) > stop_condition_f_val) or (abs(calculate_f2(x0[0], x0[1], x0[2])) > stop_condition_f_val) or (abs(calculate_f3(x0[0], x0[1], x0[2]) > stop_condition_f_val))):
        J0 = [[calculate_f1_x1(x0[0]), calculate_f1_x2(x0[1]), calculate_f1_x3(x0[2])],
        [calculate_f2_x1(x0[0]), calculate_f2_x2(x0[2]), calculate_f2_x3(x0[2])],
        [calculate_f3_x1(x0[0]), calculate_f3_x2(x0[1]), calculate_f3_x3(x0[2])]]
        f00 = [calculate_f1(x0[0], x0[1], x0[2]), calculate_f2(x0[0], x0[1], x0[2]), calculate_f3(x0[0], x0[1], x0[2])]
        J = np.array(J0)
        f0 = np.array(f00)
        J.reshape(shape)
        try:
            invJ = inv(J)
            x0 -= np.dot(invJ, f0)
        except np.linalg.linalg.LinAlgError:
            x0 = "Singular_matrix"
            break
        i += 1
    roots = roots + (x0, i)
    return roots