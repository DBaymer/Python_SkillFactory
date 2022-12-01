# Найти через рекурсивную функцию минимальный элемент списка:
# L = [i for i in range(10)]
L = [3, 5, 7, 8, 1]


def min_list(m):
    if len(m) == 1:
        return m[0]
    return m[0] if m[0] < min_list(m[1:]) else min_list(m[1:])


print(min_list(L))
