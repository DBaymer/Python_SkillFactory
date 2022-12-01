# Использование условных операторов:
a = None or input("Введите значение:")
b = None or input("Введите значение:")

if a and b:
    print("Обе переменные истинные")
    print(a, b)

elif a or b:
    print("Одна из переменных истинная")
    print(a or b)
else:
    print("Обе переменные ложные")
