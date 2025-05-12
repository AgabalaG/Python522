import json

def load_data(filename="countries.json"):
    """Loads data from a JSON file.  If the file doesn't exist, returns an empty dictionary."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:  #Handle possible errors if the file has been tampered with.
        print("Error: The data file is corrupted.  Starting with an empty database.")
        return {}


def save_data(data, filename="countries.json"):
    """Saves data to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)  #Added indent for readability


def add_data(data):
    """Adds a new country and capital to the dictionary."""
    country = input("Введите название страны (с заглавной буквы): ")
    capital = input("Введите название столицы страны (с заглавной буквы): ")
    data[country] = capital
    print("Файл сохранен")
    return data

def delete_data(data):
    """Deletes a country from the dictionary."""
    country = input("Введите название страны для удаления (с заглавной буквы): ")
    if country in data:
        del data[country]
        print("Данные удалены.")
    else:
        print("Страна не найдена.")
    return data


def search_data(data):
    """Searches for a country and prints its capital."""
    country = input("Введите название страны для поиска (с заглавной буквы): ")
    if country in data:
        print(f"Столица страны {country}: {data[country]}")
    else:
        print("Страна не найдена.")


def edit_data(data):
    """Edits the capital of an existing country."""
    country = input("Введите название страны для редактирования (с заглавной буквы): ")
    if country in data:
        new_capital = input(f"Введите новое название столицы для страны {country} (с заглавной буквы): ")
        data[country] = new_capital
        print("Данные обновлены.")
    else:
        print("Страна не найдена.")
    return data


def view_data(data):
    """Prints the entire dictionary of countries and capitals."""
    print(data)


def main():
    """Main function to run the program."""
    data = load_data()

    while True:
        print("*" * 20)
        print("Выбор действия:")
        print("1 - добавление данных")
        print("2 - удаление данных")
        print("3 - поиск данных")
        print("4 - редактирование данных")
        print("5 - просмотр данных")
        print("6 - завершение работы")
        print("*" * 20)

        choice = input("Ввод: ")

        if choice == '1':
            data = add_data(data)
            save_data(data)
        elif choice == '2':
            data = delete_data(data)
            save_data(data)
        elif choice == '3':
            search_data(data)
        elif choice == '4':
            data = edit_data(data)
            save_data(data)
        elif choice == '5':
            view_data(data)
        elif choice == '6':
            print("Завершение работы.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие от 1 до 6.")


if __name__ == "__main__":
    main()
