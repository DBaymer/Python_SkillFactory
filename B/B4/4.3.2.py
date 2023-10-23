# Написать функцию, которая будет перемножать любое количество заданных аргументов:
a = [1, 2, 3, 4, 5]


def work(*nums):
    w = 1
    for n in nums:
        w *= n

    return w


print(work())
print(work(a))
print(work(*a))
print(work(1, 2, 3, 4, 5))
