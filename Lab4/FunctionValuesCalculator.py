import math
import numpy as np

__author__ = 'Wiktor'


@np.vectorize
def calculate_f_x(x, k=3, m=1):
    # return x * math.sin((k * math.pi)/x)
    return math.exp((-k) * math.sin(m * x)) + k * math.sin(m * x) - 1
    # return math.exp((-k) * math.sin(m * x)) + k * math.cos(m * x)


def calculate_f_p_x(x, k=3, m=1):
    return k * m * math.cos(m*x) - k * m * math.exp(-k * math.sin(m*x)) * math.cos(m*x)