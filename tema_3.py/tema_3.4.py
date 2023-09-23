word = str(input("введите предложение"))
glas = "aeiou"

len = len(word)
print(f"длинна предложения: {len}")

low = word.lower()
print(f"предложение в нижнем регистре: {low}")

col = sum(low.count(vowel) for vowel in glas)
print(f"количество глассных: {col}")

zam = low.replace("ugly", "beauty")
print(f"слова заменины: {zam}")

if low.startswith("the"):
    print("Программа начинается с `the`")

if low.endswith("end"):
    print("программа заканчивается `end`")