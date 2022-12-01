# Зеркально развернуть число. В числе не должно быть нулей:
n = int(123456789)


def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res


print(mirror(n))
