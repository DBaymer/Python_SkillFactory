# Найти наибольший элемент в матрице
matrix = [
    [1, 2, 3],
    [7, -1, 2],
    [123, 2, -1]
]
max_value_mt = []
max_index_mt = []

# for row in matrix:
#     max_index = 0
#     max_value = max_index
#     for index in range(len(row)):
#         max_v = index
#         print(max_v)


for row in matrix:
    max_index = 0
    max_value = row[max_index]
    for index in range(len(row)):
        if row[index] > max_value:
            max_value = row[index]
            max_index = index
        # print(max_value)
        # print(max_index)
    max_value_mt.append(max_value)
    max_index_mt.append(max_index)
print("Максимальный элемент:", max_value_mt)
print("Индекс максимального элемента:", max_index_mt)
