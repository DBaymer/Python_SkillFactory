string = input("Введите числа через пробел:")

list_of_strings = string.split()  # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings))  # список целых int чисел

print(sum(list_of_numbers[::3]))  # sum() вычисляет сумму элементов списка с шагом 3
