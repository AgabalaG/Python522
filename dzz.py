class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}"


class Student(Human):
    def __init__(self, name, age, group, course):
        super().__init__(name, age)
        self.group = group
        self.course = course

    def display_info(self):
        return f"{super().display_info()}, Группа: {self.group}, Курс: {self.course}"


class Teacher(Human):
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)
        self.subject = subject
        self.experience = experience

    def display_info(self):
        return f"{super().display_info()}, Предмет: {self.subject}, Стаж: {self.experience} лет"


class Graduate(Student):
    def __init__(self, name, age, group, course, thesis):
        super().__init__(name, age, group, course)
        self.thesis = thesis

    def display_info(self):
        return f"{super().display_info()}, Тема диплома: {self.thesis}"


people = [
    Student("Батодалаев Даши", 16, "ГК Web_011", 5),
    Human("Загидуллин Линар", 32),
    Student("Шугани Сергей", 15, "РПО PD_011", 5),
    Teacher("Даньшин Андрей", 38, "Астрофизика", 10),
    Student("Маркин Даниил", 17, "ГК Python_011", 5),
    Graduate("Башкиров Алексей", 45, "Разработка приложений", 20, "Защита персональных данных"),
]

for person in people:
    print(person.display_info())
