# Цикл по возведению в степень числа
n = 10  # Максимальное значение
i = 1  # Начальное значение
while i ** 2 < n:  # Возводим в степень и проверяем условие: не стало ли число > n
    i += 1  # Размер шага, добавляем +1 к начальному числу, если предыдущее условие выполняется
print(i)  # Выводим на экран максимальное число, после которого цикл прекратил выполнение
