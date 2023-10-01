results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

# Сортировка результатов по возрастанию
sorted_results = sorted(results, reverse=False)

# Вывод трех лучших результатов
top_three_results = sorted_results[:3]
print("Три лучших результата:")
for result in top_three_results:
    print(result)

# Сортировка результатов по убыванию
sorted_results = sorted(results, reverse=True)

# Вывод трех худших результатов
top_three_results = sorted_results[:3]
print("Три худших результата:")
for res in top_three_results:
    print(res)

# Сортировка результатов по возрастанию
sorted_results = sorted(results, reverse=False)

# Вывод всех результатов начиная с 10
print("Все результаты начиная с 10:")
for all in sorted_results:
    print(all)