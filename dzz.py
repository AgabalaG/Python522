class Account:
    def __init__(self, owner, account_number, balance):
        """Инициализатор класса"""
        self._owner = owner              # Фамилия владельца
        self._account_number = account_number  # Номер счета
        self._balance = balance            # Сумма в рублях

    # Вариант 1: Использование декоратора @property
    @property
    def owner(self):
        """Get метод для владельца счета"""
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        """Set метод для владельца счета"""
        if isinstance(new_owner, str):
            self._owner = new_owner
        else:
            raise ValueError("Владелец должен быть строкой.")

    # Вариант 2: Использование get_...() и set_...()
    def get_balance(self):
        """Get метод для баланса"""
        return self._balance

    def set_balance(self, new_balance):
        """Set метод для баланса"""
        if isinstance(new_balance, (int, float)):
            if new_balance >= 0:
                self._balance = new_balance
            else:
                raise ValueError("Баланс не может быть отрицательным.")
        else:
            raise TypeError("Баланс должен быть числом.")

# Пример использования класса
account = Account("Иванов И.И.", "123456789", 10000)

# Использование @property
print(f"Владелец: {account.owner}")  # Получение
account.owner = "Петров П.П."         # Установка
print(f"Новый владелец: {account.owner}")

# Использование get_...() и set_...()
print(f"Баланс: {account.get_balance()}")  # Получение
account.set_balance(15000)                 # Установка
print(f"Новый баланс: {account.get_balance()}")
