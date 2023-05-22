# Вывести на экран силу ветра в зависимости от его скорости.
# Ожидаем целое число int
speed = int(input("Введите скорость ветра в м/с: "))
if speed <= 0:
    print("Stihl")
# Для более чёткого диапазона лучше использовать скобки и операторы типа and
elif (speed >= 1) and (speed <= 4):
    print("Weak")
elif (speed >= 5) and (speed <= 10):
    print("Moderate")
elif (speed >= 11) and (speed <= 18):
    print("Strong")
else:
    print("Hurricane")
