def fib(maxi):
    f1, f2 = 0, 1
    while f1 < maxi:
        yield f1
        f1, f2 = f2, f1 + f2

print sum(filter(lambda n: n % 2 == 0, fib(4000000)))
