# Функция-генератор для бесконечной последовательности натуральных чисел
def count(start=1, step=1):
    counter = start
    while True:
        yield counter
        counter += step


# Не доделано, не очень понимаю практическое применение
