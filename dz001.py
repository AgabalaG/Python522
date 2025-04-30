import abc
import math

class Shape(abc.ABC):
    def __init__(self, color):
        self.color = color

    @abc.abstractmethod
    def calculate_perimeter(self):
        pass

    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass

    def display_info(self):
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.calculate_area()}")
        print(f"Периметр: {self.calculate_perimeter()}")
        self.draw()


class Square(Shape):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_area(self):
        return self.side ** 2

    def draw(self):
        for i in range(self.side):
            print("*" * self.side)


class Rectangle(Shape):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_area(self):
        return self.length * self.width

    def draw(self):
        for i in range(self.width):
            print("*" * self.length)


class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def draw(self):
        for i in range(1, int(self.calculate_perimeter() / 3) + 1):
            print("*" * i)


square = Square(side=3, color="red")
print("===Квадрат===")
print(f"Сторона: {square.side}")
square.display_info()

rectangle = Rectangle(length=3, width=7, color="green")
print("\n===Прямоугольник===")
print(f"Длина: {rectangle.length}")
print(f"Ширина: {rectangle.width}")
rectangle.display_info()

triangle = Triangle(side1=11, side2=2, side3=6, color="yellow")
print("\n===Треугольник===")
print(f"Сторона 1: {triangle.side1}")
print(f"Сторона 2: {triangle.side2}")
print(f"Сторона 3: {triangle.side3}")
triangle.display_info()

