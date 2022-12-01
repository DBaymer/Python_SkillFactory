# Проверить совпадает ли сумма цифр числа n с числом s:
t = int(123)
g = int(6)


def equal(n, s):
    if s < 0:
        return False
    if n < 10:
        return n == s
    else:
        return equal(n // 10, s - n % 10)


print(equal(t, g))
