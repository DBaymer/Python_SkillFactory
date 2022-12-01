# Добавить класс Circle с параметром радиус и метод для расчёта площади:
# Прямоугольник
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


# Квадрат
class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2


# Круг
class Circle:
    def __init__(self, a):
        self.a = a

    def get_area_circle(self):
        return (self.a ** 2) * 3.14


rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
square_1 = Square(5)
square_2 = Square(10)
circle_1 = Circle(1)
circle_2 = Circle(2)

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]  # Соберём фигуры в список
# Методом for пройдёмся по списку. Метод isinstance проверяет соответствие.
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_area_circle())
