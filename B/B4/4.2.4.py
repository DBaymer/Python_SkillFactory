# Печатаем обратную лесенку для числа n:
# n = 3
# ***
# **
# *
n = int(input("Введите число:"))


def reverse_stair(m):
    for i in range(m, 0, -1):  # Обратная последовательность от n до 1
        print("*" * i)


reverse_stair(n)
