# Оптимизировать код
# Шкала по y и x от -10 до 10
# if x > 0:
#     if y > 0:  # x > 0, y > 0
#         print("Первая четверть")
#     else:  # x > 0, y < 0
#         print("Четвёртая четверть")
# else:
#     if y > 0:  # x < 0, y > 0
#         print("Вторая четверть")
#     else:  # x < 0, y < 0
#         print("Третья четверть")

# Введём переменные и сразу преобразуем входные данные к числам:
x = int(input("Введите x:"))
y = int(input("Введите y:"))
# Дальше обычное сравнение:
if (x > 0) and (y > 0):
    print("Первая четверть")
if (x < 0) and (y > 0):
    print("Вторая четверть")
if (x < 0) and (y < 0):
    print("Третья четверть")
if (x > 0) and (y < 0):
    print("Четвёртая четверть")
