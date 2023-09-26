def process_values(*args):
    i = len(args)

    ss = sum(args)

    print("среднее арифметическое: ", int(ss/i))


user_values = input("Введите значения через пробел: ").split()

user_values = [int(val) for val in user_values]

process_values(*user_values)
