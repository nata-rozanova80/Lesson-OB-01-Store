import sys

class Store:
    # Создаем пустой список магазинов
    store_list = []

    def __init__(self, name, address):
        self.name = name          # Название магазина
        self.address = address    # Адрес магазина
        self.items = {}          # Инициализация пустого словаря
        Store.store_list.append(self)  # Добавление нового магазина в список

    @classmethod # 1
    def list_store(cls):
        print("Список магазинов:")
        if cls.store_list:  # Проверка на непустоту списка
            for store in cls.store_list:
                print(f"Название: {store.name}, Адрес: {store.address}")
        else:
            print("Список пуст.")  # Сообщение, если список пуст

    @classmethod #2
    def add_store(cls):
        while True:  # Цикл для повторных запросов
            print("Добавление нового магазина...")
            name = input("Введите название магазина: ")
            address = input("Адрес: ")
            store = cls(name, address)  # Создаем новый экземпляр Store

            while True:  # Цикл для добавления товаров
                user_input = input("Добавить товары? (да/нет): ").strip().lower()  # Запрос на ввод от пользователя
                if user_input == "да":
                    print("tuta")
                    store.add_item()  # Вызов процедуры добавления товара
                    break  # Выход из цикла добавления товаров, если товары были добавлены
                elif user_input == "нет":
                    break  # Выход из цикла добавления товаров, если товары не нужны
                else:
                    print("Пожалуйста, введите 'да' или 'нет'.")

            # После добавления магазина и товаров
            another_store = input("Хотите добавить еще один магазин? (да/нет): ").strip().lower()
            if another_store != "да":
                break  # Выход из цикла добавления магазинов

        @classmethod ##3
        def add_item(cls):
            print ("in add_item")
            while True:  # Цикл для добавления товаров
                item_name = input("Введите название товара (или 'выход' для завершения): ").strip()
                if item_name.lower() == 'выход':
                    user_input4 = input("Вернуться к добавлению магазина? (да/нет): ").strip().lower()  # Запрос на ввод от пользователя
                    if user_input4 == 'да':
                        Store.add_store()
                    break  # Выход из цикла, если пользователь хочет завершить добавление товаров

                try:
                    price = float(input("Введите цену товара: "))
                    cls.items[item_name] = price  # Добавление товара в словарь
                    print(f"Товар '{item_name}' с ценой {price} добавлен.")
                except ValueError:
                    print("Пожалуйста, введите корректное значение цены.")

        def remove_item(self): #4
            item_name = input("Введите название товара, который хотите удалить: ").strip()
            if item_name in self.items:
                del self.items[item_name]  # Удаление товара из словаря
                print(f"Товар '{item_name}' успешно удален.")
            else:
                print(f"Товар '{item_name}' не найден.")

        def item_price(self): #  5
            item_name = input("Введите название товара, цену которого хотите узнать: ").strip()
            if item_name in self.items:
                price = self.items[item_name]  # Получаем цену товара из словаря
                print(f"Цена '{item_name}' составляет '{price}' рублей.")
            else:
                print(f"Товар '{item_name}' не найден.")

        def price_change(self): # 6
            item_name = input("Введите название товара, цену которого хотите изменить: ").strip()
            if item_name in self.items:
                price = self.items[item_name]  # Получаем цену товара из словаря
                print(f"Цена '{item_name}' составляет '{price}' рублей.")
                user_input3 = input("Изменить цену? (да/нет): ").strip().lower()  # Запрос на ввод от пользователя
                if user_input3 == 'да':
                    try:
                        new_price = float(input("Введите новую цену товара: "))  # Запрашиваем новую цену
                        self.items[item_name] = new_price  # Обновляем цену товара в словаре
                        print(f"Цена товара '{item_name}' успешно изменена на {new_price} рублей.")
                    except ValueError:
                        print("Пожалуйста, введите корректное значение цены.")
            else:
                print(f"Товар '{item_name}' не найден.")

def start_work(): #7
    while True:
        print(f"\nМЕНЮ ПРОГРАММЫ")
        print(f"1. Список всех магазинов")
        print(f"2. Добавить магазин")
        print(f"3. Добавить товары")
        print(f"4. Удалить товары")
        print(f"5. Цена товара")
        print(f"6. Изменить цену товара")
        print(f"7. Выход")

        number = input("Выберите номер действия: ")

        if number == "1":
            Store.list_store()
        elif number == "2":
            Store.add_store()
        elif number == "3":
            store_name = input("Введите название магазина, в который хотите добавить товары: ").strip()
            store = next((s for s in Store.store_list if s.name == store_name), None)
            if store:
                store.add_item()
            else:
                print("Магазин не найден.")
        elif number == "4":
            store_name = input("Введите название магазина, из которого хотите удалить товары: ").strip()
            store = next((s for s in Store.store_list if s.name == store_name), None)
            if store:
                store.remove_item()
            else:
                print("Магазин не найден.")
        elif number == "5":
            store_name = input("Введите название магазина, в котором хотите узнать цену товара: ").strip()
            store = next((s for s in Store.store_list if s.name == store_name), None)
            if store:
                store.item_price()
            else:
                print("Магазин не найден.")
        elif number == "6":
            store_name = input("Введите название магазина, в котором хотите изменить цену товара: ").strip()
            store = next((s for s in Store.store_list if s.name == store_name), None)
            if store:
                store.price_change()
            else:
                print("Магазин не найден.")
        elif number == "7":
            print("Выход из программы.")
            sys.exit()
        else:
            print("Некорректный ввод. Пожалуйста, выберите номер от 1 до 7.")

# Запуск программы
start_work()