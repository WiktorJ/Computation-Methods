from __future__ import division
import math
from numpy import zeros, arange
from Drawer import add_to_plot, draw_plot
from FunctionValuesCalculator import calculate_f_x_2b, calculate_differential_equation_2a

__author__ = 'wiktor'
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

def create_matrix(k, m, a, b, n, h, f):
    a_matrix = zeros(shape=(n+1, 3))
    b_matrix = zeros(shape=(n+1, 1))

    a_matrix[0] = [0, 2 + h*h*m*m , -1]
    b_matrix[0] = 2*m*math.cos(m*a)*h*h + 1

    a_matrix[n] = [-1, 2 + h*h*m*m, 0]
    b_matrix[n] = 2*m*math.cos(m*b)*h*h + calculate_f_x_2b(b, k, m)
    x = [float(a)]
    t = a + h
    factors = [-1, m*m*h*h + 2, -1]
    for i in range(1, n):
        t += h
        x.append(t)
        a_matrix[i] = factors
        b_matrix[i] = -h*h*f(t, k, m)
    x.append(b)
    x.reverse()
    return (a_matrix, b_matrix, x)



def transform_matrix_to_row_echelon_form(amatrix, bmatrix, equationNumber):
    for i in range(0, equationNumber-1):
        tmp = amatrix[i][1]
        for j in range(1, len(amatrix[0])):
            amatrix[i][j] = amatrix[i][j] / tmp
        bmatrix[i] = bmatrix[i]/tmp
        tmp = amatrix[i+1][0]
        for j in range(0, len(amatrix[0]) - 1):
            amatrix[i+1][j] = amatrix[i+1][j] - tmp*amatrix[i][j+1]
        bmatrix[i+1] = bmatrix[i+1] - bmatrix[i]*tmp
    bmatrix[equationNumber-1] = bmatrix[equationNumber - 1]/amatrix[equationNumber-1][1]
    amatrix[equationNumber-1][1] = amatrix[equationNumber - 1][1]/amatrix[equationNumber-1][1]


def solve_linear_equation(amatrix, bmatrix, equationNumber):
    prev = 0
    solution = []
    for i in range(int(equationNumber)-1, -1, -1):
        solution.append(bmatrix[i, 0] - prev * amatrix[i][2])
        prev = bmatrix[i, 0] - prev * amatrix[i][2]
    return solution


def solve_equation(p, q, r, x_a, x_b, y_a, y_b, n, method_name, draw_flag, m):
    h = (x_b-x_a) / float(n)
    xs = map(lambda j: x_a + h*j, range(1, n))
    # create matrix
    b = map(lambda x: -h*h*r(x), xs)
    b[0] += (1.0 + h/2.0 * p(xs[0])) * y_a
    b[-1] += (1.0 - h/2.0 * p(xs[-1])) * y_b

    a = map(lambda x: -1.0 + h*p(x)/2.0, xs[:-1])
    d = map(lambda x: 2 + h*h*q(x), xs)
    c = map(lambda x: -1.0 - h*p(x)/2.0, xs[1:])

    # solve (thomas)

    for k in range(1, n-1):
        quot = a[k-1] / d[k-1]
        d[k] -= quot * c[k-1]
        b[k] -= quot * b[k-1]

    x0 = map(lambda x: 0,range(n-1))
    x0[n-2] = b[n-2] / d[n-2]

    for k in range(n-3, -1, -1):
        x0[k] = (b[k] - c[k] * x0[k+1]) / d[k]

    xs.insert(0,x_a)
    xs.append(x_b)

    x0.insert(0,y_a)
    x0.append(y_b)

    f_y = []
    xx = arange(x_a, x_b, 0.1)
    for i in xs:
        f_y.append(calculate_f_x_2b(i, k, m))
    mean_square_error = calculate_mean_square_error(xs,f_y, x0)
    max_error = calculate_max_norm(xs, f_y, x0)
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
        add_to_plot(xs, calculate_f_x_2b(xs, k, m), "given f")
        add_to_plot(xs, x0, "Finite difference method")
        file_name = method_name + "_"+str(n)
        title = method_name + "  n = "+str(n)+"\n mean square error = " + mean_format.format(mean_square_error) + "\n max error = " + max_format.format(max_error)
        draw_plot(title, file_name)


def go():
    k = 2
    m = 3
    a = 0
    b = (2*math.pi + 2)/m
    n = 1000
    p = lambda x: 0.0
    q = lambda x: -m*m
    r = lambda x: -2*m * math.cos(m * x)
    y_exact = lambda x: math.cos(m*x) - x*math.sin(m*x)
    y_a = 1
    y_b = y_exact(b)
    print("n;mean square error; max error")
    i = 5
    step = 1
    while i <= n:
        if i < 10:
            step = 1
        elif 10 <= i < 100:
            step = 10
        else:
            step = 50
        solve_equation(p, q, r, a, b, y_a, y_b, i, "Finite_difference_method", True, m)
        i += step



go()