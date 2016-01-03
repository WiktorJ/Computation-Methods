import math
import numpy as np

__author__ = 'Wiktor'


@np.vectorize
def calculate_f_x(x, k=3, m=1):
    # return x * math.sin((k * math.pi)/x)
    return math.exp((-k) * math.sin(m * x)) + k * math.sin(m * x) - 1
    # return math.exp((-k) * math.sin(m * x)) + k * math.cos(m * x)
    # return math.sqrt(x)