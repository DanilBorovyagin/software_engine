try:
    with open("3.txt", "r") as f:
        content = f.read()
        if content:
            print("содержимое файла: ")
            print(content)
        else:
            raise Exception("файл пустой ")
except Exception as ex:
    print(ex)
