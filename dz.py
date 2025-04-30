import json

data = {
    "1441751072": {
        "name": "ebeqbqa",
        "tel": "7979251508"
    },
    "6384137383": {
        "name": "daeefed",
        "tel": "6253294228"
    },
    "8186377272": {
        "name": "bdbqeab",
        "tel": "9543402193"
    },
    "7194236131": {
        "name": "gafdbee",
        "tel": "6265065413"
    },
    "3313812937": {
        "name": "gbfddgg",
        "tel": "5668240979"
    }
}

# Пример использования:
# Вывод данных в формате JSON с отступами для читаемости
print(json.dumps(data, indent=4))

# Пример доступа к данным:
# Получение имени по ключу
key = "1441751072"
if key in data:
    name = data[key]["name"]
    print(f"Имя для ключа {key}: {name}")
else:
    print(f"Ключ {key} не найден.")

# Пример итерации по данным
for key, value in data.items():
    name = value["name"]
    tel = value["tel"]
    print(f"Ключ: {key}, Имя: {name}, Телефон: {tel}")

