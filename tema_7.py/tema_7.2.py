with open("expenses.txt", "a") as file:
    file.write(input("Введите данные о расходах:"))
    file.write("\n")
with open("expenses.txt", "r") as file:
    content = file.read()
print(content)