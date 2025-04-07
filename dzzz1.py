class Account:
    # Статические свойства
    exchange_rate_usd = 75.0  # Курс рубля по отношению к доллару
    exchange_rate_eur = 90.0   # Курс рубля по отношению к евро

    def __init__(self, owner, account_number, interest_rate, balance):
        """Инициализатор класса"""
        self.owner = owner              # Фамилия владельца
        self.account_number = account_number  # Номер счета
        self.interest_rate = interest_rate    # Процент начисления
        self.balance = balance            # Сумма в рублях
        self.is_closed = False            # Состояние счета (открыт/закрыт)

    def __del__(self):
        """Деструктор"""
        print(f"Банковский счет {self.account_number} закрыт.")

    @classmethod
    def update_exchange_rate(cls, new_rate_usd, new_rate_eur):
        """Редактировать курс рубля по отношению к доллару и евро"""
        cls.exchange_rate_usd = new_rate_usd
        cls.exchange_rate_eur = new_rate_eur

    @staticmethod
    def convert_to_usd(rub_amount):
        """Перевод суммы в доллары"""
        return rub_amount / Account.exchange_rate_usd

    @staticmethod
    def convert_to_eur(rub_amount):
        """Перевод суммы в евро"""
        return rub_amount / Account.exchange_rate_eur

    def change_owner(self, new_owner):
        """Смена владельца счета"""
        self.owner = new_owner

    def withdraw(self, amount):
        """Снятие заданной суммы"""
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            print("Недостаточно средств.")
            return 0

    def calculate_interest(self):
        """Начисление процентов на баланс"""
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return interest

    def info(self):
        """Вывод информации о счете"""
        status = "Открыт" if not self.is_closed else "Закрыт"
        return f"Владелец: {self.owner}, Номер счета: {self.account_number}, Баланс: {self.balance} руб., Статус: {status}"

# Пример использования класса
account = Account("Иванов И.И.", "123456789", 5, 10000)
print(account.info())
account.withdraw(1000)
print(f"Баланс после снятия: {account.balance} руб.")
account.calculate_interest()
print(f"Баланс после начисления процентов: {account.balance} руб.")
print(f"Сумма в долларах: {Account.convert_to_usd(account.balance)} USD")

