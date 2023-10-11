user = input("введите предложение")
use = user.lower()


with open("ignor.txt", "r") as f:
    content = f.read()
    content_list = content.split()

for word in content_list:
    rep = "*" * len(word)
    use = use.replace(word, rep, -1)

print(use)