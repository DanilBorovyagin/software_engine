from collections import *

with open("lol.txt", "r") as files:
    content = files.read()
    worlds = len(content.split())
    sp = content.split()
    sp = [word for word in sp if len(word) >= 3]
    count = Counter(sp)
    most = count.most_common(1)[0][0]
    most_1 = count.most_common(1)[0][1]

print("кол-во слов:", worlds)
print("самое частое слово", most, f"встречается в тексте {most_1} раз")