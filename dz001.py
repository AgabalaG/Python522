import json

# Модель
class Film:
    def __init__(self, название, жанр, режиссер, год_выпуска, длительность, студия, актеры):
        self.название = название
        self.жанр = жанр
        self.режиссер = режиссер
        self.год_выпуска = год_выпуска
        self.длительность = длительность
        self.студия = студия
        self.актеры = актеры

    def __str__(self):
        return (f"Название: {self.название}\n"
                f"Жанр: {self.жанр}\n"
                f"Режиссер: {self.режиссер}\n"
                f"Год выпуска: {self.год_выпуска}\n"
                f"Длительность: {self.длительность}\n"
                f"Студия: {self.студия}\n"
                f"Актеры: {self.актеры}")


# Контроллер
class FilmController:
    def __init__(self, view):
        self.films = []
        self.view = view
        self.filename = "films.json"  # Имя файла для хранения данных

    def загрузить_фильмы(self):
        """Загружает фильмы из JSON файла."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                film_data = json.load(f)
                for film_dict in film_data:
                    film = Film(**film_dict) # Создаем экземпляр Film из словаря
                    self.films.append(film)
        except FileNotFoundError:
            print("Файл с фильмами не найден. Начинаем с пустого каталога.")
            self.films = []
        except json.JSONDecodeError:
            print("Ошибка декодирования JSON. Возможно, файл поврежден.")
            self.films = []

    def сохранить_фильмы(self):
         """Сохраняет фильмы в JSON файл."""
         film_data = []
         for film in self.films:
             film_data.append(film.__dict__) # Преобразуем объект Film в словарь
         with open(self.filename, 'w', encoding='utf-8') as f:
             json.dump(film_data, f, indent=4, ensure_ascii=False)


    def добавить_фильм(self):
        название = self.view.запросить_данные("Название фильма: ")
        жанр = self.view.запросить_данные("Жанр: ")
        режиссер = self.view.запросить_данные("Режиссер: ")
        год_выпуска = self.view.запросить_данные("Год выпуска: ")
        длительность = self.view.запросить_данные("Длительность: ")
        студия = self.view.запросить_данные("Студия: ")
        актеры = self.view.запросить_данные("Актеры: ")

        film = Film(название, жанр, режиссер, год_выпуска, длительность, студия, актеры)
        self.films.append(film)


        self.сохранить_фильмы() # Сохраняем изменения в файл
        self.view.показать_сообщение("Фильм добавлен!")


    def показать_каталог(self):
        if not self.films:
            self.view.показать_сообщение("Каталог фильмов пуст.")
            return

        for i, film in enumerate(self.films):
            self.view.показать_сообщение(f"{i+1}. {film.название}")


    def показать_фильм(self):
        if not self.films:
            self.view.показать_сообщение("Каталог фильмов пуст.")
            return

        self.показать_каталог()
        try:
            index = int(self.view.запросить_данные("Введите номер фильма для просмотра: ")) - 1
            if 0 <= index < len(self.films):
                self.view.показать_сообщение(str(self.films[index]))
            else:
                self.view.показать_сообщение("Неверный номер фильма.")
        except ValueError:
            self.view.показать_сообщение("Неверный ввод. Введите число.")

    def удалить_фильм(self):
        if not self.films:
            self.view.показать_сообщение("Каталог фильмов пуст.")
            return

        self.показать_каталог()
        try:
            index = int(self.view.запросить_данные("Введите номер фильма для удаления: ")) - 1
            if 0 <= index < len(self.films):
                del self.films[index]
                self.сохранить_фильмы()  # Сохраняем изменения в файл
                self.view.показать_сообщение("Фильм удален.")
            else:
                self.view.показать_сообщение("Неверный номер фильма.")
        except ValueError:
            self.view.показать_сообщение("Неверный ввод. Введите число.")

# Представление (View)
class FilmView:
    def запросить_данные(self, prompt):
        return input(prompt)

    def показать_сообщение(self, message):
        print(message)


# Главная функция (клиентский код)
def main():
    view = FilmView()
    controller = FilmController(view)
    controller.загрузить_фильмы()  # Загружаем фильмы при запуске программы

    while True:
        print("\n====== Редактирование данных каталога фильмов ======")
        print("Действия с фильмами:")
        print("1 - добавление фильма")
        print("2 - каталог фильмов")
        print("3 - просмотр определенного фильма")
        print("4 - удаление фильма")
        print("q - выход из программы")

        выбор = view.запросить_данные("Выберите вариант действия: ")

        if выбор == '1':
            controller.добавить_фильм()
        elif выбор == '2':
            controller.показать_каталог()
        elif выбор == '3':
            controller.показать_фильм()
        elif выбор == '4':
            controller.удалить_фильм()
        elif выбор.lower() == 'q':
            controller.сохранить_фильмы()  # Сохраняем фильмы перед выходом
            print("Выход из программы.")
            break
        else:
            view.показать_сообщение("Неверный вариант действия.")

if __name__ == "__main__":
    main()


