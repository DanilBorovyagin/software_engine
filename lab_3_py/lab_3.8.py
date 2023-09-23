val = 0
while val < 100:
    if val == 0:
        val += 10
    elif val // 5 >= 2:
        val *= 5
    else:
        val -= 5
    print(val)
