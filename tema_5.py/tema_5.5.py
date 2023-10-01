list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]


def transform_list(i):
    result = set()
    result.update(generate_combinations(i))
    result.update(set(i))
    return result


def generate_combinations(num_list):
    combinations = set()
    for num in num_list:
        count = num_list.count(num)
        if count > 1:
            for i in range(2, count + 1):
                combinations.add(str(num) * i)
    return combinations


result_1 = transform_list(list_1)
result_2 = transform_list(list_2)
result_3 = transform_list(list_3)
print(f"{result_1}\n{result_2}\n{result_3}")