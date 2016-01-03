__author__ = 'Wiktor'

def lagrange_interpolate(points):
    def result_polynomial(x):
        sum = 0
        n = len(points)
        for i in xrange(n):
            xi, yi = points[i]
            product = 1
            for j in xrange(n):
                if i != j:
                    xj, yj = points[j]
                    product *= (x - xj)/float(xi - xj)
            sum += yi * product
        return sum
    return result_polynomial
