def fib(n):
    a = 1
    b = 1

    for _ in range(n):
        yield a
        c = a
        a = b
        b = c + b


fibon = fib(1000)
for num in fibon:
    print(num)
