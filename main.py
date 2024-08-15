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

    @classmethod
    def add_item(cls):
        while True:  # Цикл для добавления товаров
            item_name = input("Введите название товара (или 'выход' для завершения): ").strip()
            if item_name.lower() == 'выход':
                break  # Выход из цикла, если пользователь хочет завершить добавление товаров

            try:
                price = float(input("Введите цену товара: "))
                cls.items[item_name] = price  # Добавление товара в словарь
                print(f"Товар '{item_name}' с ценой {price} добавлен.")
            except ValueError:
                print("Пожалуйста, введите корректное значение цены.")

    @classmethod
    def remove_item(cls):
        item_name = input("Введите название товара, который хотите удалить: ").strip()
        if item_name in cls.items:
            del cls.items[item_name]  # Удаление товара из словаря
            print(f"Товар '{item_name}' успешно удален.")
        else:
            print(f"Товар '{item_name}' не найден.")

    @classmethod
    def item_price(cls):
        item_name = input("Введите название товара, цену которого хотите узнать: ").strip()
        if item_name in cls.items:
            price = cls.items[item_name]  # Получаем цену товара из словаря
            print(f"Цена '{item_name}' составляет '{price}' рублей.")
        else:
            print(f"Товар '{item_name}' не найден.")


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
            Store.remove_item()
        elif number == "5":
            Store.item_price()
        elif number == "6":
            Store.add_task()
        elif number == "7":
            print("Выход из программы.")
            sys.exit() # Завершение работы программы
        else:
            print("Некорректный ввод. Пожалуйста, выберите номер от 1 до 7.")
# Запуск программы
start_work()
