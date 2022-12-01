# Найти количество делителей для числа a:
c = int(input("Введите число:"))


def get_multipliers(a):
    count = 0  # Счётчик по умолчанию = 0
    for n in range(1, a + 1):  # Последовательность от 1 до a, последнее число не включается
        if a % n == 0:
            count += 1

    return count  # Почему-то не выводит значение
    # print(count)


t = get_multipliers(5)
print(t)
