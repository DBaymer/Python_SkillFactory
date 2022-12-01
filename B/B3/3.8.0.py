# Найти минимум и максимум в каждой строке матрицы
matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]
min_value_rows = []  # Список для минимальных элементов в ряду
min_index_rows = []  # Список индексов минимальных элементов
max_value_rows = []  # Список максимальных элементов
max_index_rows = []  # Список индексов максимальных элементов
for row in matrix:  # Цикл, который проходит по всем строкам матрицы
    min_index = 0  # Начальный индекс
    min_value = row[min_index]  # Минимальное значение = индексу минимального числа в строке
    max_index = 0  # Начальный индекс
    max_value = row[max_index]  # Максимальное значение = индексу максимального числа в строке
    for index_col in range(len(row)):  # Цикл для перебора индексов в строке
        if row[index_col] < min_value:  # Если число меньше минимального значения, то переменные перезаписываются
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:  # # Если число больше максимального значения, то переменные перезаписываются
            max_value = row[index_col]
            max_index = index_col
    min_value_rows.append(min_value)  # Добавляем найденные значения в списки
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)
print("Минимальный элемент:", min_value_rows)
print("Индексы минимальных элементов:", min_index_rows)
print("Максимальные элементы:", max_value_rows)
print("Индексы максимальных элементов:", max_index_rows)
