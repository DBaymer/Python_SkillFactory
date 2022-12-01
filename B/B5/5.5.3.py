# Отсортировать список со значениями массы и роста по индексу массы тела:
# Вес, рост
data = [
    (82, 1.91),
    (68, 1.74),
    (90, 1.89),
    (73, 1.79),
    (76, 1.84)
]

print(sorted(data, key=lambda x: x[0] / (x[1]*100)**2))

# Найти кортеж с минимальным индексом массы тела:
print(min(data, key=lambda x: x[0] / x[1]**2))  # отбор по ключу
