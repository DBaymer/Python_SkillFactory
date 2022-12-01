# Определить является ли строка палиндромом:
text = input("Введите текст:")


def check_palindrome(string):
    n = string
    string = string.lower()
    string = string.replace(" ", "")
    if string == string[::-1]:
        print(f"{n} - палиндром")
    else:
        print(f"{n} - не палиндром")


check_palindrome(text)
