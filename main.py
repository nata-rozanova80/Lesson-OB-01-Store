#  Создай класс `Store`:
# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.

class Store:
    # Создаем пустой список для хранения задач
    task_list = []

    def __init__(self, name, address, items):  # 1) Method
        self.name = name          # Название магазина
        self.address = address  # Адрес магазина
        self.items = {}  # Инициализация пустого словаря


    # # Пример использования
    # my_instance = MyClass()
    # print(my_instance.items)  # Выведет: {}
#     def display_dict(self):
#         # Метод для отображения содержимого словаря
#         for key, value in self.my_dict.items():
#             print(f"{key}: {value}")
#
# # Пример использования класса
# obj = MyClass()
# obj.display_dict()