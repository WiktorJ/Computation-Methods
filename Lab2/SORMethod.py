from __future__ import division
import random
from numpy import zeros, diag, diagflat, dot, inf, arange, array
from numpy.linalg import linalg
import copy
# zminne sa rozmiar ukadu, warunek stopu ro, wektor poczatkowy
# zbadac: dokladnosc, liczba iteracji, czas obliczen
__author__ = 'Wiktor'


def create_matrix(m, k, p, N, iteration_number, starting_conditions,w):
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
    x = copy.copy(starting_conditions)
    x_norm = p + 1
    i = 0
    B = R/D
    e_vals, e_vect = linalg.eig(B)
    # print(";".join((str(N), str(max(abs(e_vals))))))
    # print "results for ||x(i+1) - x(i): "
    while (x_norm >= p) and (i < iteration_number):
        prev_x = x.copy()
        for j in range(0, N):
            d = 0
            for k in range(0, N):
                if j != k:
                    d = d + A[j][k] * x[k]
            x[j] = (1 - w) * x[j] + (w/A[j][j])*(b[j] - d)
        x_norm = linalg.norm(x - prev_x, inf)  # norma typu max po kolumnach
        i += 1
    print(";".join((str(w), str("%.1e" % p), str(N), str(i), str("%.3e" % linalg.norm(x_copy - x)),
                    str("%.3e" % linalg.norm(x_copy - x, inf)))) + ";"),
    x = x_copy
    b = dot(A, x)
    x = starting_conditions
    b_norm = p + 1
    i = 0
    # print "results for ||Ax(i) -b ||"
    while (b_norm >= p) and (i < iteration_number):
        for j in range(0, N):
            d = 0
            for k in range(0, N):
                if j != k:
                    d = d + A[j][k] * x[k]
            x[j] = (1 - w) * x[j] + (w/A[j][j])*(b[j] - d)
        b_norm = linalg.norm(dot(A, x) - b, inf)
        i += 1
    print(";".join((str(i), str("%.3e" % linalg.norm(x_copy - x)), str("%.3e" % linalg.norm(x_copy - x, inf)))))


def jacobi():
    N = 180
    size = 100

    m = 1
    k = 7
    step = 40
    st = [[random.uniform(-2, 2) for _ in range(0, 3)]]
    for i in range(43, N, step):
        st.append([random.uniform(-2, 2) for _ in range(0, i)])
    # print("starting conditions: 0 vector")
    print("w;stop_condition;N;iter;euclidean_norm;max_norm;"
          "iter;euclidean_norm;max_norm")
    for w in arange(0.6, 1.9, 0.3):
        p = 0.1
        for i in range(3, N, step):
            starting_conditions = zeros(shape=i)
            create_matrix(m, k, p, i, size, starting_conditions, w)

        p = 0.001
        for i in range(3, N, step):
            starting_conditions = zeros(shape=i)
            create_matrix(m, k, p, i, size, starting_conditions, w)

        p = 0.00000001
        for i in range(3, N, step):
            starting_conditions = zeros(shape=i)
            create_matrix(m, k, p, i, size, starting_conditions, w)

        # print "starting conditions: random vector in range (-2,2)"
        # p = 0.1
        # j = 0
        # for i in range(3, N, step):
        #     starting_conditions = st[j]
        #     create_matrix(m, k, p, i, size, array(starting_conditions), w)
        #     j += 1
        #
        # p = 0.001
        # j = 0
        # for i in range(3, N, step):
        #     starting_conditions = st[j]
        #     create_matrix(m, k, p, i, size, array(starting_conditions), w)
        #     j += 1
        #
        # p = 0.00000001
        # j = 0
        # for i in range(3, N, step):
        #     starting_conditions = st[j]
        #     create_matrix(m, k, p, i, size, array(starting_conditions), w)
        #     j += 1


jacobi()