user = input("1:информация о сотруднике\n2:добавление нового сотрудника\n3:просмотр всего файла\nвыберите действие ")

if user == "2":
    while True:
        users = input("введите 1 для продолжения добавления сотрудников или введите 2 для завершения ")

        if users == "2":
            break

        id = input(str("Введите id сотрудника: "))
        fio = input(str("Введите ФИО сотрудника: "))
        age = input(str("Введите возраст сотрудника: "))
        status = input(str("Введите статус сотрудника: "))
        company = input(str("Введите компанию сотрудника: "))
        with open("id.txt", "a") as f:
            content = f.write("id " + id + ": " + "ФИО:" + fio + ", " + "возвраст:" + age + "лет, " + "статус:" + status + ", " + "компания:" + company + "." + "\n")

elif user == "1":
    id_user = input("введите id сотрудника: ")
    with open("id.txt", "r") as f:
        lin = f.readlines()
        for line in lin:
            if line.startswith(f"id {id_user}"):
                print(line)
                break
        else:
            print("Введенного id нет в базе данных.")

elif user == "3":
    with open("id.txt", "r") as f:
        file = f.read()
        print(file)

else:
    print("не верное значение")