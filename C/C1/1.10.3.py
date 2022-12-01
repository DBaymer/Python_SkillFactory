# Создать класс клиент с данными: имя, фамилия, город, баланс.
# Вывести на экран.
class Customers:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.first_name} {self.second_name}. {self.city}. Баланс: {self.balance} руб."'


customer_1 = Customers('Иван', 'Петров', 'Тюмень', 50)
print(customer_1)
