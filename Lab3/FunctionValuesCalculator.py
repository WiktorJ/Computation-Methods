from IPython.core.display import Math
import math
import numpy as np

__author__ = 'Wiktor'


@np.vectorize
def calculate_f_x(x, n, m):
    return (x - 1) * math.exp(-m * x) + pow(x, n)


def calculate_f_p_x(x, n, m):
    return -m * x * math.exp(-m * x) + math.exp(-m * x) + m * math.exp(-m * x) + n * pow(x, n - 1)


def calculate_f1(x1, x2, x3):
    return float(x1)*float(x1) - 4.*x2*x2 + float(x3)*float(x3)*float(x3) - 1.


def calculate_f2(x1, x2, x3):
    return 2.*x1*x1 + 4.*x2*x2 - 3.*x3


def calculate_f3(x1, x2, x3):
    return float(x1)*float(x1) - 2.*x2 - float(x3)*float(x3) - 1.


def calculate_f1_x1(x1):
    return 2.*x1


def calculate_f1_x2(x2=0):
    return -8.*x2


def calculate_f1_x3(x3=0):
    return 3.*x3*x3


def calculate_f2_x1(x1=0):
    return 4.*x1


def calculate_f2_x2(x2=0):
    return 8.*x2


def calculate_f2_x3(x3):
    return -3.


def calculate_f3_x1(x1):
    return 2.*x1


def calculate_f3_x2(x2):
    return -2.


def calculate_f3_x3(x3):
    return -2.*x3