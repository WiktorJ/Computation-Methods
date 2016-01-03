import copy

__author__ = 'Wiktor'


def newton_interpolate(points):
    x1, y1 = zip(*points)
    c = copy.deepcopy(list(y1))
    x = copy.deepcopy(list(x1))
    n = len(points)
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            c[j] = (c[j] - c[j - 1]) / (x[j] - x[j - i])
    def result_polynomiall(xpoint):
        val = c[0]
        factor = 1.0
        for i in range(1, n):
            factor *= (xpoint - x[i - 1])
            val += (c[i] * factor)
        return val
    return result_polynomiall