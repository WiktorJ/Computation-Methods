from random import randint
from numpy import arange

__author__ = 'Wiktor'
from NonlinearNewtonMethod import *


def solve_system(starting_vector, p):
    max_iteration = 1000
    (x1, i1, x2, i2) = calculate_root_newton(starting_vector, p, p, max_iteration)
    starting_vector = [float("{:1.1f}".format(x)) for x in starting_vector]
    print ";".join((str(x1), str(i1), str(x2), str(i2), str(p),  str(starting_vector)))


def start():
    print "NM root1;iter;NM root2;iter;accuracy;starting_vector"

    for i in range(3, 6):
        for j in range(-3, 4):
            starting_vector = [float(j)*randint(1, 10), float(j)*randint(1, 10), float(j)*randint(1, 10)]
            solve_system(starting_vector, pow(10, -2 * i))
        for j in arange(-1, 1, 0.2):
            starting_vector = [float(j)*randint(1, 6), float(j)*randint(1, 3), float(j)*randint(1, 6)]
            solve_system(starting_vector, pow(10, -2 * i))



start()
