# Все операции - деление строки по пробелам, преобразование к числам
# и приведение объекта map к типу список, можно делать в одной строке
L = list(map(float, input().split()))

# Обмениваем первое и последнее число
# с помощью множественного присваивания
# работа идёт с индексами
L[0], L[-1] = L[-1], L[0]

# Находим сумму sum и добавляем .append ее в конец списка
L.append(sum(L))

print(L)
