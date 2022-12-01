# Исправить код, чтобы он завершался, когда будет найден первый отрицательный элемент списка
list_ = [1, 2, 3, -1, 3, 2, 1, 2, 3, 2, 1, 0, 0, 0, -1, 2]
negate_index = -1
negate_value = 0
for i, val in enumerate(list_):
    if val < 0:
        negate_index = i
        negate_value = val
        break

print(f'{negate_index}: {negate_value}')
