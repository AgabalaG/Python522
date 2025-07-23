import requests
from bs4 import BeautifulSoup
import csv

class WebScraper:
    """
    Базовый класс для веб-скрейпера.
    """
    def __init__(self, base_url, csv_filename="output.csv"):
        """
        Инициализирует скрейпер.

        Args:
            base_url (str): Базовый URL веб-сайта.
            csv_filename (str, optional): Имя файла CSV для сохранения данных.
                                         По умолчанию "output.csv".
        """
        self.base_url = base_url
        self.csv_filename = csv_filename
        self.all_data = []  # Список для хранения всех собранных данных

    def get_page_content(self, url):
        """
        Получает содержимое страницы по указанному URL.

        Args:
            url (str): URL страницы.

        Returns:
            BeautifulSoup: Объект BeautifulSoup для разбора HTML, или None в случае ошибки.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Проверка на ошибки HTTP
            return BeautifulSoup(response.content, "html.parser")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении страницы {url}: {e}")
            return None

    def extract_data(self, soup):
      """
      Извлекает данные с текущей страницы
      """
      pass # будет определено в классах-наследниках

    def save_data_to_csv(self):
        """
        Сохраняет собранные данные в CSV файл.
        """
        with open(self.csv_filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            if self.all_data:
               #предполагаем что у всех элементов all_data одинаковая структура
               header = self.all_data[0].keys()
               writer.writerow(header)

               for row in self.all_data:
                   writer.writerow(row.values())
            print(f"Данные сохранены в {self.csv_filename}")

    def run(self, max_pages=5):
      """
      Запускает процесс скрейпинга.
      """
      for page_num in range(1, max_pages + 1):
        url = f"{self.base_url}/catalogue/page-{page_num}.html"  # Шаблон URL для страниц
        soup = self.get_page_content(url)

        if soup:
          page_data = self.extract_data(soup)
          if page_data:
             self.all_data.extend(page_data)
        else:
          break #Если страница не загрузилась, прекращаем сканирование

      self.save_data_to_csv() # сохраняем все, что собрали

class BookScraper(WebScraper):
  """
  Специализированный класс для извлечения данных о книгах с конкретного сайта
  """
  def __init__(self, base_url, csv_filename="books.csv"):
        super().__init__(base_url, csv_filename)

  def extract_data(self, soup):
      """
      Извлекает данные о книгах со страницы.

      Args:
          soup (BeautifulSoup): Объект BeautifulSoup для разбора HTML.

      Returns:
          list: Список словарей с данными о книгах.
      """
      books = []
      product_pods = soup.find_all("article", class_="product_pod")
      for pod in product_pods:
          title = pod.h3.a["title"]
          price = pod.find("p", class_="price_color").text
          books.append({"title": title, "price": price})
      return books

if __name__ == "__main__":
  # Пример использования
  base_url = "https://books.toscrape.com"  # Замените на ваш базовый URL
  book_scraper = BookScraper(base_url, "books.csv")
  book_scraper.run(max_pages=3)  # Извлечь данные с 3 страниц

# pip install requests beautifulsoup4
# python book_scraper.py
