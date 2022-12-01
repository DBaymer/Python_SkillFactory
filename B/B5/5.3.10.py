# Проверить входящее число на ряд условий:
# all работает при условии, что все условия верны (оператор and)
a = int(input("Введите число:"))

if all([type(a) == int,
        100 <= a <= 999,
        a % 2 == 0,
        a % 3 == 0]):
    print("Число удовлетворяет условиям")
else:
    print("Число не удовлетворяет условиям")

# Для проверики на хотя бы 1 условие нужно использовать оператор (any) = (or)
