# Создадим кортеж
shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])  # Получим id последнего элемента кортежа
print(shopping_center)  # Вывести кортеж
# Добавим append название в конец списка [-1]
shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])  # Получим id последнего элемента кортежа
print(shopping_center)  # Вывести кортеж

# Сравним, полученные ранее id
print(list_id_before == list_id_after)
