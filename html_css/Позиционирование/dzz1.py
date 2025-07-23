import requests
from bs4 import BeautifulSoup
import csv

def scrape_and_save_to_csv(url, csv_filename="output.csv"):
    """
    Извлекает данные с указанного URL и сохраняет их в CSV файл.

    Аргументы:
        url (str): URL веб-сайта для извлечения данных.
        csv_filename (str, optional): Имя CSV файла для сохранения. По умолчанию "output.csv".
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Вызвать исключение для плохих кодов статуса

        soup = BeautifulSoup(response.content, "html.parser")

        # Измените этот раздел, чтобы извлечь конкретные данные, которые вам нужны
        # Пример: Извлечение всего текста параграфов
        data = [p.get_text(strip=True) for p in soup.find_all("p")]

        # Запись в CSV
        with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            # Записать заголовок (опционально, зависит от ваших данных)
            # Пример: writer.writerow(["Текст"])
            # Записать данные
            for row in data:
                writer.writerow([row])

        print(f"Данные извлечены и сохранены в {csv_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении URL: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    target_url = "https://www.example.com"  # Замените на ваш целевой URL
    scrape_and_save_to_csv(target_url)

# pip install requests beautifulsoup4
# python scraper.py
