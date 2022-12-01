# Собрать переменную из цифр, введённых из консоли
numbers = input("Enter numbers separated by a space:")
# Разбиваем на подстроки получившийся результат
numbers_split = numbers.split()
# Разносим на строки \n получившийся результат .join
numbers_lines = "\n".join(numbers_split)

print(numbers_lines)
