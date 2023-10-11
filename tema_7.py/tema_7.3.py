import string

with open("latin.txt","r") as file:
    content = file.read()
    worlds = len(content.split())

    content = content.lower()
    content = content.translate(str.maketrans("","", string.punctuation))
    lis = list(content)
    while " " in lis:
        lis.remove(" ")
    while "\n" in lis:
        lis.remove("\n")
    bukvi = len(lis)

    line = content.splitlines()
    kol = len(line)

print(bukvi, "буквы")
print(worlds, "слова")
print(kol, "строки")
