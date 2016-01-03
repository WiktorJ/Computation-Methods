import math
import numpy as np

__author__ = 'Wiktor'


@np.vectorize
def calculate_f_x_1(x, k=3, m=1):
    return math.exp((-k) * math.cos(m * x)) - k * math.cos(m * x) + 1


@np.vectorize
def calculate_f_x_2b(x, k, m):
    return math.cos(m*x)-x*math.sin(m*x)



def calculate_differential_equation(x, y, k=0, m=0):
    return k*k*m*math.sin(m*x)*math.cos(m*x) + k*m*y*math.sin(m*x)
    # return y - x*x + 1


def calculate_differential_equation_2a(x, k, m):
    return -2*m*math.cos(m * x)