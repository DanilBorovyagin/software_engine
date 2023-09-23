string = "hello"
value = [0, 2, 4, 6, 8, 10]
counter = 0
while " world" not in string:
    memory = string
    if counter in value:
        string = string + " world"
    print(string)
    if counter < 10:
        string = memory
    counter += 1
