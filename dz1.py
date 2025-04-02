import os
import shutil

def move_empty_files(root_dir):
    """
    Находит все пустые файлы в заданном дереве каталогов,
    перемещает их в директорию work/empty_files, и выводит
    сообщения о перемещении.
    """

    empty_files_dir = os.path.join(root_dir, "work/empty_files")
    os.makedirs(empty_files_dir, exist_ok=True) # Создаем, если не существует

    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                file_size = os.path.getsize(file_path)
                if file_size == 0:
                    # Пустой файл
                    new_path = os.path.join(empty_files_dir, file)
                    relative_path = os.path.relpath(file_path, root_dir)  # Путь относительно root_dir

                    shutil.move(file_path, new_path)

                    print(f"Перемещен файл: {file}")
                    print(f"Старый путь: {relative_path}")
                    print(f"Новый путь: work/empty_files/{file}")  # Жестко задаем путь к пустой папке
                    print("-" * 20) # Разделитель
            except FileNotFoundError:
                print(f"Файл не найден: {file_path}")  # Обработка ошибки, если файл удален

# Пример использования (замените "." на фактический корневой каталог, если нужно)
move_empty_files(".")


def list_non_empty_files(root_dir):
    """
    Находит и выводит имена и размеры всех непустых файлов в дереве каталогов.
    """
    print("Непустые файлы:")
    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                if file_size > 0:  # Проверяем, что файл не пустой
                    print(f"'{os.path.relpath(file_path, root_dir)}' - {file_size} bytes")
            except FileNotFoundError:
                print(f"Файл не найден: {file_path}")

# Пример использования (замените "." на фактический корневой каталог, если нужно)
list_non_empty_files(".")
