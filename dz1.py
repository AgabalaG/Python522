import json
import csv

def json_to_csv(json_filepath, csv_filepath):


    try:
        with open(json_filepath, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print(f"Ошибка: Файл {json_filepath} не найден.")
        return
    except json.JSONDecodeError:
        print(f"Ошибка: Не удалось декодировать JSON из файла {json_filepath}. Проверьте формат.")
        return

    if not isinstance(data, list):
        print("Ошибка: JSON файл должен содержать список объектов.")
        return


    if data:
        fieldnames = data[0].keys()

        try:
            with open(csv_filepath, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(data)
            print(f"Данные успешно записаны в {csv_filepath}")

        except Exception as e:
            print(f"Ошибка при записи в CSV-файл: {e}")
    else:
        print("JSON файл пуст.")


json_filepath = 'todos.json'  # Замените на имя вашего JSON файла
csv_filepath = 'todos.csv'    # Замените на имя вашего CSV файла
json_to_csv(json_filepath, csv_filepath)
