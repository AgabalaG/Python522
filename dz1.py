import math

class Pair:
    """
    Класс, представляющий пару чисел.
    """
    def __init__(self, a, b):
        """
        Инициализация пары чисел.
        """
        self.a = a
        self.b = b

    def change_numbers(self, new_a, new_b):
        """
        Изменение чисел в паре.
        """
        self.a = new_a
        self.b = new_b

    def calculate_product(self):
        """
        Вычисление произведения чисел в паре.
        """
        return self.a * self.b

    def calculate_sum(self):
        """
        Вычисление суммы чисел в паре.
        """
        return self.a + self.b

class RightTriangle(Pair):
    """
    Класс, представляющий прямоугольный треугольник, унаследованный от Pair.
    """
    def __init__(self, a, b):
        """
        Инициализация прямоугольного треугольника.
        """
        super().__init__(a, b)  # Вызов конструктора родительского класса

    def calculate_hypotenuse(self):
        """
        Вычисление гипотенузы треугольника.
        """
        return math.sqrt(self.a**2 + self.b**2)

    def calculate_area(self):
        """
        Вычисление площади треугольника.
        """
        return 0.5 * self.a * self.b

    def display_info(self):
        """
        Вывод информации о треугольнике на экран.
        """
        hypotenuse = self.calculate_hypotenuse()
        print(f"Прямоугольный треугольник с катетами: {self.a} и {self.b}")
        print(f"Гипотенуза: {hypotenuse:.2f}")
        print(f"Площадь: {self.calculate_area():.2f}")

# Демонстрация работы классов
# Создание объекта класса Pair
pair = Pair(5, 8)
print("Работа с классом Pair:")
print(f"Сумма: {pair.calculate_sum()}")
print(f"Произведение: {pair.calculate_product()}")
pair.change_numbers(10, 20)
print(f"Новая сумма: {pair.calculate_sum()}")
print(f"Новое произведение: {pair.calculate_product()}")

# Создание объекта класса RightTriangle
triangle = RightTriangle(5, 8)
print("\nРабота с классом RightTriangle:")
triangle.display_info()

# Пример с другими значениями
triangle.change_numbers(3, 4)
print("\nИзменение катетов треугольника:")
triangle.display_info()

