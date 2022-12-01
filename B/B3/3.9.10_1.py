# Решение от программистов
# Определить есть ли в числе цифра 5
number = 186678
digitToFind = 5

num = number
while num > 0:
    digit = num % 10
    if digit == digitToFind:
        print(f"{digitToFind} is in number {number}")
        break
    num = int(num / 10)
