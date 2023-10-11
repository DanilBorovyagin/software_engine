with open("expenses.txt", "a") as f:
    f.write("\nсоль морская 80 рублей")

with open("expenses.txt", "r") as f:
    res = f.read()
    print(res)