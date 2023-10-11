lin = ["one", "two", "three"]
with open("w.txt", "w") as f:
    for line in lin:
        f.write("\nprank " + line)
    print("готово!")