try:
    user = input("Введите число для сложения: ")


    def sumi(user1):
        res = int(user1) + 2
        return res


    result = sumi(user)
    print(result)
except ValueError:
    print("Не подходящий тип данных. Ожидалось число")

