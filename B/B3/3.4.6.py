# Определить является ли число палиндромом
number = input("Введите число:")
# Введённые данные преобразуем в строку
string = str(number)
if string == string[::-1]:  # Сравниваем строку и её обратный порядок
    print(f"{number} - палиндром")  # f"{переменная}" отправит значение переменной в строку вывода
else:
    print(f"{number} - обычное число")
