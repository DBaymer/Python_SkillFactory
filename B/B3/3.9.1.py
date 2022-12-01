# Найти индекс последнего отрицательного элемента в списке
list_ = [-5, 2, 4, 8, 12, -7, 5]
# Переменная для записи индекса отрицательного элемента
index_negative = None

# for i in range(len(list_)):
#     if list_[i] < 0:
#         print("Отрицательное число:", list_[i])
#         index_negative = i  # Перезаписываем значение индекса
#         print("Новый индекс отрицательного числа:", index_negative)
#     else:
#         print("Положительное число:", list_[i])
#     print("---")
# print("Конец цикла")
# print()
# print("Индекс последнего отрицательного элемента =", index_negative)

# А теперь то же самое, только с функцией enumerate

for i, value in enumerate(list_):
    if value < 0:
        print("Отрицательное число:", value)
        index_negative = i  # Перезаписываем значение индекса
        print("Новый индекс отрицательного числа:", index_negative)
    else:
        print("Положительное число:", value)
    print("---")
print("Конец цикла")
print()
print("Индекс последнего отрицательного элемента =", index_negative)
