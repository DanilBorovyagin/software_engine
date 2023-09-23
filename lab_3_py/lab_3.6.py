string = "Счастливых голодных игр"
value = input("введите букву для поиска")
for i in string:
    if i == value:
        index = string.find(value)
        print(f"буква {value} найдена в индексе {index}")
        break
else:
    print(f"буква {value} не найдена")