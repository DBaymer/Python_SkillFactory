# Исправить код:
employee = 5
i = 1
while i < employee:
    if i > 1:
        print('There are', i, 'people in the department')  # В отделе i человек
    if i == 1:
        print('There are', i, 'people in the department')  # В отделе i человек
    i += 1  # Не хватало этой строки
