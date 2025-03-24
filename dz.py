def count_negative_numbers(arr):
    """
    Вычисляет количество отрицательных чисел в массиве.

    Args:
      arr: Список чисел.

    Returns:
      Количество отрицательных чисел в массиве.
    """
    count = 0
    for num in arr:
        if num < 0:
            count += 1
    return count

# Пример использования
numbers = [-2, 3, 8, -11, -4, 6]
negative_count = count_negative_numbers(numbers)
print(f"n = {negative_count}")

#Альтернативное решение с использованием list comprehension:

def count_negative_numbers_comprehension(arr):
    """
    Вычисляет количество отрицательных чисел в массиве, используя list comprehension.
    """
    return len([num for num in arr if num < 0])

numbers = [-2, 3, 8, -11, -4, 6]
negative_count = count_negative_numbers_comprehension(numbers)
print(f"n = {negative_count}")


