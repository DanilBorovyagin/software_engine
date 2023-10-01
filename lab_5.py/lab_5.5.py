def useless(numbers):
    if not numbers:
        return None

    max_number = max(numbers)
    length = len(numbers)
    useless_value = max_number / length

    return useless_value


execution_times = [1, 50, 10, 1, 15, 3]


useless_num = useless(execution_times)

print("Бесполезное число:", useless_num)


for index, time in enumerate(execution_times):
    if time > useless_num:
        print("Шаг", index+1, "имеет продолжительность выше среднего")
    else:
        print("Шаг", index+1, "имеет продолжительность ниже или равную среднему")