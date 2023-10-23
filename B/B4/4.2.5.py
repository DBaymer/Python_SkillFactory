# Найти количество делителей для числа a:
a = int(input("Введите число: "))

def get_multipliers(a):
    count = 0  # Счётчик по умолчанию = 0
    for n in range(1, a + 1):  # Последовательность от 1 до a, последнее число не включается
        if a % n == 0:
            count += 1
    return count


print(get_multipliers(a))
