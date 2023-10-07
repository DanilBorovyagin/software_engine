def find(log_tuple, id):
    if id not in log_tuple:
        return ()
    start_index = log_tuple.index(id)

    try:
        end_index = log_tuple.index(id, start_index + 1)
    except ValueError:
        end_index = len(log_tuple)

    return log_tuple[start_index:end_index]


log_1 = (1, 2, 3)
id_1 = 8
result_1 = find(log_1, id_1)
print(result_1)

log_2 = (1, 8, 3, 4, 8, 8, 9, 2)
id_2 = 8
result_2 = find(log_2, id_2)
print(result_2)

log_3 = (1, 2, 8, 5, 1, 2, 9)
id_3 = 8
result_3 = find(log_3, id_3)
print(result_3)