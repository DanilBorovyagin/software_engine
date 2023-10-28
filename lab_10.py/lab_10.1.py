from functools import *
import time


def time1(func):
    def wra(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"\nВремя выполнения функции {func.__name__}: {execution_time} секунд")
        return result
    return wra

@time1
@lru_cache(None)
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


result = fib(100)
print(result)


@time1
def fib1(n):
    if n <= 1:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


result = fib1(100)
print(result)

