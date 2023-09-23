val = 0
for i in range(3):
    for j in range(3):
        if i != j:
             val += j
        else:
            pass

print(val)