def main(one, two, four, free):
    res = one + two
    sum1 = four * free
    return sum1


for _ in range(4):
    x = 4
    y = 44
    a = 444
    b = 2
    an = main(x, a, y, b)
    print(an)
an1 = main(4, 44, 444, 4444)
print(an1)