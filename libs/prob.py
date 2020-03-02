from math import factorial


def binom(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
