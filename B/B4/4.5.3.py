# Написать декоратор, который будет сохранять результаты в словаре
# При повторном вызове брать значения из словаря, а не вычислять заново
def cache(func):
    cache_dict = {}

    def wrapper(num):
        nonlocal cache_dict
        if num not in cache_dict:
            cache_dict[num] = func(num)
            print(f"Добавление результата в кэш: {cache_dict[num]}")
        else:
            print(f"Возращение результата из кэша: {cache_dict[num]}")
        print(f"Кэш {cache_dict}")
        return cache_dict[num]

    return wrapper


@cache
def f(n):
    return n * 123456789


print(f(123))
print(f(356))
print(f(123))
