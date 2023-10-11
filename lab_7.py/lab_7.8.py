import os


def print_doc(directory):
    all = os.walk(directory)
    for catalog in all:
        print(f"папка {catalog[0]} содержит:")
    print(f'директория: {catalog[1]}')
    print(f'Файлы: {catalog[2]}')
    print("-" * 40)

print_doc("I:")