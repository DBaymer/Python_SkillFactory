# При помощи генератора списков создать таблицу умножения чисел от 1 до 10
T = [[i*j for j in range(1, 11)] for i in range(1, 11)]
print(T)

# Можно составить список из кортежей
list_tuples = [(i, i**2) for i in range(1,11)]
print(list_tuples)

# Можно создать матрицу «одним махом»
M = [[i+j for j in range(5)] for i in range(5)]
print(M)
