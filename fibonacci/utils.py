def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_fast(n - 2)


def fib_fast(n):
    nth_fib = [0] * (n + 2)
    nth_fib[1] = 1
    for i in range(2, n + 1):
        nth_fib[i] = nth_fib[i - 1] + nth_fib[i - 2]
    return nth_fib[n]

