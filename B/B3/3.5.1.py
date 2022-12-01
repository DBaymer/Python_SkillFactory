# Пример множественных вложений условий
# Нужно выбрать форму одежды при разных погодных условиях
temperature = int(input("Введите температуру:"))

# Начальные статусы дождя None
rainy = None
heavyRain = None

# При крайних температурах никакого желания гулять
decision = "Останусь дома."
if (temperature >= 30) or (temperature <= -30):
    print(decision)
# Надо дописать скрипт, чтобы дальше не продолжалась программа

# Если температура < 0 - дождь маловероятен
if temperature > 0:
    rainy = input("Идёт дождь?:") == "yes"
# Если дождь есть, то на сколько он сильный
    if rainy:
        heavyRain = input("Сильный дождь?:") == "yes"

# Дальше пошла реализация логики по диапазону температур
if (temperature > 20) and (temperature < 30):
    if rainy:
        decision = "Футболка + шорты и дождевик"
    else:
        decision = "Футболка + шорты"
elif temperature > 0:
    if rainy:
        if heavyRain:
            decision = "Пальто, резиновые сапоги и зонт"
        else:
            decision = "Пальто и дождевик"
    else:
        decision = "Надеть пальто"
else:
    decision = "Только пуховик!"

# Решение на экран
print(decision)
