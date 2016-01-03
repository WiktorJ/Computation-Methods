from __future__ import division
import math
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
__author__ = 'wiktor'


def euclidean_error(u1, u2, n, m):
    result = 0;
    for i in range(0, m):
        for j in range(0, n):
            # result += math.sqrt((u1[j, i] - u2[j, i]) * (u1[j, i] - u2[j, i]))
            if abs((u1[j, i] - u2[j, i])) > result:
                result = abs((u1[j, i] - u2[j, i]))
    return result
def calculate_next_value(r, prev, n, u_0t, u_at):

    s = 1 - 2*r
    b = prev[1:-1]

    b[0] -= r * u_0t
    b[-1] -= r * u_at

    n -= 2

    a = [r for x in range(n-1)]
    d = [s for x in range(n)]
    c = [r for x in range(n-1)]

    for k in range(1, n-1):
        quot = a[k-1] / d[k-1]
        d[k] -= quot * c[k-1]
        b[k] -= quot * b[k-1]


    x0 = [0 for x in range(n)]
    x0[n-2] = b[n-2] / d[n-2]
    for k in range(n-3, -1, -1):
        x0[k] = (b[k] -c[k] * x0[k+1]) / d[k]

    x0.insert(0,u_0t)
    x0.append(u_at)
    return x0


def implicit_method(ax, bx, at, bt, n, m, phi, psi1, psi2,a):
    h = (bx - ax)/n
    k = (bt - at)/m

    xs = [x * h for x in range(0, n)]
    ts = [x * k for x in range(0, m)]

    r = -a*a*k/(h*h)

    u = np.zeros((n, m))

    for i in range(0, n):
        u[i, 0] = phi(xs[i])

    prev = [u[i, 0] for i in range(0, n)]

    for j in range(1, m):
        next = calculate_next_value(r, prev, n, psi1(ts[j]), psi2(ts[j]))
        for i in range(0, n):
            u[i, j] = next[i]
            prev = next
    return xs, ts, u, r



def explicit_method(ax, bx, at, bt, n, m, phi, psi1, psi2,a):
    h = (bx - ax)/n
    k = (bt - at)/m

    xs = [x * h for x in range(0, n)]
    ts = [x * k for x in range(0, m)]

    r = a*a*k/(h*h)
    s = 1 - 2*r

    u = np.zeros((n, m))

    for i in range(0, m):
        u[0, i] = psi1(ts[i])
        u[n-1, i] = psi2(ts[i])

    for i in range(1, n-1):
        u[i, 0] = phi(xs[i])

    for j in range(1, m):
        for i in range(1, n-1):
            u[i, j] = s * u[i, j-1] + r * (u[i-1, j-1] + u[i+1, j-1])


    return xs, ts, u, r


def plot(filename, title, x, t, u):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    X, Y = np.meshgrid(t, x)
    surf = ax.plot_surface(X, Y, u, rstride=1, cmap=cm.jet, linewidth=0)
    ax.set_zlim(-2, 6)
    plt.xlabel('t')
    plt.ylabel('x')
    plt.title(title)
    ax.zaxis.set_major_locator(LinearLocator(5))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    ax.view_init(azim=-70, elev=10)
    # plt.show()
    fig.colorbar(surf)
    plt.savefig("charts/" + filename + '.png')


def start():
    A = 1
    w = 1
    a = 2

    phi = lambda x: 0
    psi1 = lambda t:A*t;
    # psi1 = lambda t: A * t;
    # psi2 = lambda t: math.sin(w * t)
    psi2 = lambda t: math.exp(-t) *  math.sin(w*t)
    # phi = lambda x: math.sin(x)
    # psi1= lambda t: 0
    # psi2 = lambda t: 0
    np.set_printoptions(threshold=np.nan)

    ax = 0
    bx = 6
    # bx = 3 * math.pi
    at = 0
    bt = 2 * math.pi
    # bt = 5
    n = 45
    m = 2900
    # n = 3000
    # m = 3000
    x, t, u1, r = explicit_method(ax, bx, at, bt, n, m, phi, psi1, psi2,a)
    # plot("explicit_method-{}-{}".format(n,m), "explicit n = {}, m = {}, r = {:.5f}".format(m, n, abs(r)), x,t,u1)
    x, t, u2,r = implicit_method(ax, bx, at, bt, n, m, phi, psi1, psi2,a)
    # plot("implicit_method-{}-{}".format(n,m), "implicit, n = {}, m = {}, r = {:.5f}".format(m, n, abs(r)), x,t,u2)
    print(euclidean_error(u1,u2,n,m))
start()





