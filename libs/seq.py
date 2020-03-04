def fib(n, scalar):
    f0, fn = 0, 1
    for _ in range(1, n):
        f0, fn = fn, f0 * scalar + fn
    return n if n < 1 else fn


def fib_gen(n, scalar):
    f0, fn = 0, 1
    for i in range(n + 1):
        if i < 2:
            yield i * scalar
        else:
            f0, fn = fn, f0 * scalar + fn
            yield fn
