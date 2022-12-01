# Вернуть дискриминант и корни квадратного уравнения:
def de(a, b, c):
    return b**2 - 4*a*c


def quadratic_solve(a, b, c):
    if de(a, b, c) < 0:
        return "Нет вещественных корней"
    elif de(a, b, c) == 0:
        return -b / (2*a)
    else:
        return (-b - de(a, b, c)**0.5) / (2*a), (-b + de(a, b, c)**0.5) / (2*a)


print(de(1, 3, 2))
print(quadratic_solve(1, 3, 2))
