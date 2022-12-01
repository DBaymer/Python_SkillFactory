# Решить уравнение:
def linear_solve(a, b):
    if a:
        return b / a
    elif not a and not b:
        return "Бесконечное количество корней"
    else:
        return "Нет корней"


# 2*x = 9
print(linear_solve(2, 9))

# 0*x = 1
print(linear_solve(0, 1))
