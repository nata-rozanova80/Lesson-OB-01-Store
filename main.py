#  Создай класс `Store`:
# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
import sys
class Store:
    # Создаем пустой список магазинов
    store_list = []

    def __init__(self, name, address, items):  # 1) Method
        self.name = name          # Название магазина
        self.address = address  # Адрес магазина
        self.items = {}  # Инициализация пустого словаря

    def list_store(self, store_list):
        print("Список магазинов:")
        for store in Store.store_list:
            if store_list:  # Проверка на непустоту списка
                print(store_list)  # Печать списка, если он не пустой
            else:
                print("Список пуст.")  # Сообщение, если список пуст

        # Функция для добавления нового магазина

    @classmethod
    def add_store(cls):
        while True:  # Цикл для повторных запросов
            print("Добавление нового магазина...")
            name = input("Введите название магазина: ")
            address = input("Адрес: ")

            while True:  # Цикл для добавления товаров
                print("Добавить товары?")
                user_input = input("Добавить товары? (да/нет): ").strip().lower()  # Запрос на ввод от пользователя

                if user_input == "да":
                    Store.add_item()  # Вызов процедуры добавления товара
                    break  # Выход из цикла добавления товаров, если товары были добавлены
                elif user_input == "нет":
                    break  # Выход из цикла добавления товаров, если товары не нужны
                else:
                    print("Пожалуйста, введите 'да' или 'нет'.")

            # После добавления магазина и товаров
            another_store = input("Хотите добавить еще один магазин? (да/нет): ").strip().lower()
            if another_store != "да":
                break  # Выход из цикла добавления магазинов



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
def start_work():
    while True:
        print(f"\nМЕНЮ ПРОГРАММЫ")
        print(f"1. Список всех магазинов")
        print(f"2. Добавить магазин")
        print(f"3. Добавить товары") # КАК ВЫБРАТЬ МАГАЗИН ДЛЯ ДОБАВЛЕНИЯ???
        print(f"4. Удалить товары")
        print(f"5. Цена товара") #метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
        print(f"6. Изменить цену товара") # метод для обновления цены товара.
        print(f"7. Выход")

        number = input("Выберите номер действия: ")

    # Выбор действия соответственно меню
        if number == "1":
            Store.list_store()
        elif number == "2":
            Store.add_store()
        elif number == "3":
            Store.add_item()
        elif number == "4":

        elif number == "2":
            Store.add_task()
        elif number == "2":
            Store.add_task()
        elif number == "5":
            print("Выход из программы.")
            sys.exit() # Завершение работы программы
        else:
            print("Некорректный ввод. Пожалуйста, выберите номер от 1 до 7.")
# Запуск программы
start_work()
