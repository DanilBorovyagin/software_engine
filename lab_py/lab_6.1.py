key = int(input("введите ключ "))
req = int(input("введите номер кабинета "))

dic = {
    10: {"ключ": key, "доступ": True},
    11: {"ключ": key, "доступ": True},
    12: {"ключ": key, "доступ": True},
    13: {"ключ": 104, "доступ": False},
    14: {"ключ": 105, "доступ": True},
    15: {"ключ": 106, "доступ": False},
    None:  {"ключ": None , "доступ": False},
}

res = dic.get(req)
if not res:
    res = dic[None]
k = res.get("ключ")
c = res.get("доступ")
print("ключ кабинета:",k, "Доступ к кабинету",c)
