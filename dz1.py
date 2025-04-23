class Student:
    def __init__(self, name, laptop_model, processor, memory):
        self.name = name
        self.laptop = self.Laptop(laptop_model, processor, memory)

    def display_info(self):
        print(f"{self.name} => {self.laptop.model}, {self.laptop.processor}, {self.laptop.memory}")

    class Laptop:
        def __init__(self, model, processor, memory):
            self.model = model
            self.processor = processor
            self.memory = memory

roman = Student("Roman", "HP", "i7", 16)
vladimir = Student("Vladimir", "HP", "i7", 16)

roman.display_info()
vladimir.display_info()
