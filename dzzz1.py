import random

class Cat:
    """
    Класс, представляющий кота.
    """
    def __init__(self, name, age, pol):
        """
        Инициализация кота.
        """
        self.name = name
        self.age = age
        self.pol = pol

    def __repr__(self):  #Для отображения в списке
        return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"

def breed_cats(cat1, cat2, expected_kittens):
    """
    Функция для "разведения" котов и кошек.
    """
    if cat1.pol == cat2.pol:
        print("Для разведения нужны кот и кошка разных полов!")
        return []

    kittens = []
    for i in range(expected_kittens):
        if random.random() < 0.5:  # С вероятностью 50% котенок будет мальчиком
            pol = 'M'
        else:
            pol = 'F'
        kittens.append(Cat(name="No name", age=0, pol=pol))
    return kittens

# Пример использования
tom = Cat(name="Tom", age=3, pol='M')
elsa = Cat(name="Elsa", age=2, pol='F')

print("Tom is good boy!!!")
print("Elsa is good girl!!!")

# Предполагаем, что хотим 2 котят
kittens = breed_cats(tom, elsa, 2)
print(kittens)

