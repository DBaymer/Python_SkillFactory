# Цикл по возведению в степень числа
n = 1  # Начальное значение
while 2 ** n < 10000:  # Возводим в степень пока условие верно
    n += 1  # Размер шага, добавляем +1 к начальному числу, если предыдущее условие выполняется
print(n)  # Выводим на экран максимальное число, после которого цикл прекратил выполнение
