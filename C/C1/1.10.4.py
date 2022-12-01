# Добавить метод, который будет выводить только имя, фамилию и город.
# Собрать полученные данные в список и вывести на экран.
class Customers:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.first_name} {self.second_name}. {self.city}. Баланс: {self.balance} руб."'

    def get_guest(self):
        return f'{self.first_name} {self.second_name}, город {self.city}'


customer_1 = Customers('Иван', 'Петров', 'Тюмень', 500)
customer_2 = Customers('Владимир', 'Зайцев', 'Курган', 100)
customer_3 = Customers('Ольга', 'Лермонтова', 'Заводоуковск', 200)

guest_list = [customer_1, customer_2, customer_3]

for guest in guest_list:
    print(guest.get_guest())
    # print(guest.__str__())
