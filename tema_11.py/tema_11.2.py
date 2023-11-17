def fib(n):
    a = 1
    b = 1

    for _ in range(n):
        yield a
        c = a
        a = b
        b = c + b


fibon = fib(10)
for num in fibon:
    with open("fib.txt", "a") as f:
        f.write(str(num))
        f.write("\n")
    print("--", num)

