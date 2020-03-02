def fib(n):
    f0, fn = 0, 1
    for _ in range(1, n):
        f0, fn = fn, f0 + fn
    return n if n < 1 else fn


def fib_gen(n):
    f0, fn = 0, 1
    for i in range(n):
        tmp = (f0, fn)
        f0 = f0 if i < 2 else tmp[1]
        fn = fn if i < 2 else tmp[0] + fn
        yield i if i < 2 else fn


def fib_ls(n):
    return [i for i in fib_gen(n)]
