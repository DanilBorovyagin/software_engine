import time


def time1(func):
    def wra():
        start_time = time.time()
        result = func()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"\nВремя выполнения функции {func.__name__}: {execution_time} секунд")
        return result
    return wra


@time1
def fib():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')


fib()
