# class Car:
#
#     def __init__(self, model_name, year_of_manufacture, manufacturer, engine_power, color, price):
#
#         self._model_name = model_name
#         self._year_of_manufacture = year_of_manufacture
#         self._manufacturer = manufacturer
#         self._engine_power = engine_power
#         self._color = color
#         self._price = price
#
#     def get_model_name(self):
#        return self._model_name
#
#     def set_model_name(self, model_name):
#         self._model_name = model_name
#
#     def get_year_of_manufacture(self):
#         return self._year_of_manufacture
#
#     def set_year_of_manufacture(self, year_of_manufacture):
#         self._year_of_manufacture = year_of_manufacture
#
#     def get_manufacturer(self):
#         return self._manufacturer
#
#     def set_manufacturer(self, manufacturer):
#         self._manufacturer = manufacturer
#
#     def get_engine_power(self):
#         return self._engine_power
#
#     def set_engine_power(self, engine_power):
#         self._engine_power = engine_power
#
#     def get_color(self):
#         return self._color
#
#     def set_color(self, color):
#         self._color = color
#
#     def get_price(self):
#         return self._price
#
#     def set_price(self, price):
#         self._price = price
#
#     def display_data(self):
#         print("********** Данные автомобиля ***********")
#         print(f"Название модели: {self._model_name}")
#         print(f"Год выпуска: {self._year_of_manufacture}")
#         print(f"Производитель: {self._manufacturer}")
#         print(f"Мощность двигателя: {self._engine_power} л.с.")
#         print(f"Цвет машины: {self._color}")
#         print(f"Цена: {self._price}")
#         print("==========================================")
#
#     def input_data(self):
#         self._model_name = input("Введите название модели: ")
#         self._year_of_manufacture = int(input("Введите год выпуска: "))
#         self._manufacturer = input("Введите производителя: ")
#         self._engine_power = int(input("Введите мощность двигателя (л.с.): "))
#         self._color = input("Введите цвет машины: ")
#         self._price = float(input("Введите цену: "))
#
#
#
# if __name__ == "__main__":
#
#     car1 = Car("X7 M50i", 2021, "BMW", 530, "white", 10790000)
#
#
#     car1.display_data()
#
#
#     car1.set_color("black")
#     car1.set_price(11000000)
#     car1.display_data()
#
#
#     car2 = Car("", 0, "", 0, "", 0)
#     car2.input_data()
#     car2.display_data()
#
#
#     print(f"Car Model Name: {car2.get_model_name()}")
#     print(f"Car Price: {car2.get_price()}")
