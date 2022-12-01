# Начинаем заполнять переменные из строки ввода:
Name = input("Название книги:")
Author = input("Автор:")
Year = input("Год издания:")
# Собираем в словарь {}
Book = {'Name': Name, 'Author': Author, 'Year': Year}
# Выводим собранные данные
print(Book)
