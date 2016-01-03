from __future__ import division
import random
from numpy import zeros, diag, diagflat, dot, inf
from numpy.linalg import linalg

# zminne sa rozmiar ukadu, warunek stopu ro, wektor poczatkowy
# zbadac: dokladnosc, liczba iteracji, czas obliczen
__author__ = 'Wiktor'


def create_matrix(m, k, p, N, iteration_number, starting_conditions):
    x = [random.choice([-1, 1]) for _ in range(0, N)]
    A = zeros(shape=(N, N))
    for i in range(0, N):
        for j in range(0, N):
            if i == j:
                A[i][j] = k
            elif j > i:
                A[i][j] = (-1) ** (j + 1) * (m / (j + 1))
            elif j == (i - 1):
                A[i][j] = m / (i + 1)
    x_copy = x
    b = dot(A, x)
    D = diag(A)
    R = A - diagflat(D)
    x = starting_conditions
    x_norm = p + 1
    i = 0
    B = R/D
    e_vals, e_vect = linalg.eig(B)
    print(";".join((str(N), str(max(abs(e_vals))))))
    # print "results for ||x(i+1) - x(i): "
    while (x_norm >= p) or (i > iteration_number):
        prev_x = x
        x = (b - dot(R, x)) / D
        x_norm = linalg.norm(x - prev_x, inf)  # norma typu max po kolumnach
        i += 1

    # print ";".join((str(N), str("%.8f" % p), str(i), str("%.15f" % linalg.norm(x_copy - x)), str("%.15f" % linalg.norm(x_copy - x, inf)))) + ";",
    x = x_copy
    b = dot(A, x)
    D = diag(A)
    R = A - diagflat(D)
    x = starting_conditions
    b_norm = p + 1
    i = 0
    # print "results for ||Ax(i) -b ||"
    while (b_norm >= p) or (i > iteration_number):
        x = (b - dot(R, x)) / D
        b_norm = linalg.norm(dot(A, x) - b, inf)
        i += 1
    # print ";".join((str(i), str("%.15f" % linalg.norm(x_copy - x)), str("%.15f" % linalg.norm(x_copy - x, inf))))



def jacobi():
    N = 150
    size = 10000
    p = 0.001
    m = 1
    k = 7
    print("starting conditions: 0 vector")
    print("N;stop_condition;iterations_criterion1;euclidean_norm_criterion1;max_norm_criterion1;"
          "iterations_criterion2;euclidean_norm_criterion2;max_norm_criterion2")
    for i in range(3, N, 20):
        starting_conditions = zeros(shape=i)
        create_matrix(m, k, p, i, size, starting_conditions)

    p = 0.1
    for i in range(3, N, 20):
        starting_conditions = zeros(shape=i)
        create_matrix(m, k, p, i, size, starting_conditions)

    p = 0.00000001
    for i in range(3, N, 20):
        starting_conditions = zeros(shape=i)
        create_matrix(m, k, p, i, size, starting_conditions)

    # print "starting conditions: random vector in range (-2,2)"
    st = [[random.uniform(-2, 2) for _ in range(0, 3)]]
    for i in range(23, N, 20):
        st.append([random.uniform(-2, 2) for _ in range(0, i)])

    p = 0.001
    j = 0
    for i in range(3, N, 20):
        starting_conditions = st[j]
        create_matrix(m, k, p, i, size, starting_conditions)
        j += 1

    p = 0.1
    j = 0
    for i in range(3, N, 20):
        starting_conditions = st[j]
        create_matrix(m, k, p, i, size, starting_conditions)
        j += 1

    p = 0.00000001
    j = 0
    for i in range(3, N, 20):
        starting_conditions = st[j]
        create_matrix(m, k, p, i, size, starting_conditions)
        j += 1


jacobi()