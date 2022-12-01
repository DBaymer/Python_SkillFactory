# С помощью рекурсии развернуть строку
def reverse_str(sting):
    if len(sting) == 0:
        return ''
    else:
        return sting[-1] + reverse_str(sting[:-1])


print(reverse_str('test'))
