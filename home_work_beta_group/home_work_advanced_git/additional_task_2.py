from typing import Callable

class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __dict__(self):
        return {
            'Наименование': self.name,
            'Стоимость': self.price,
            'Наличие': self.quantity
        }


class OnlineStore:
    def __init__(self, id: str, date: str):
        self.id = id
        self.date = date
        self.items = []

    def __dict__(self):
        return {
            'Идентификатор заказа': self.id,
            'Дата заказа': self.date,
            'Товары в заказе': self.items
        }

    def add_product(self, objekt: Callable) -> list:
        self.items.append(objekt)
        return self.items

car = Product("Машинка", 100, 500)
bacik = Product('Велосипед', 1000, 10)

user1 = OnlineStore('123', '25.11.2012')
user1.add_product(car.__dict__())
user1.add_product(bacik.__dict__())
print(user1.__dict__())


"""Функция должна возвращать словарь, содержащий информацию о средней стоимости заказа и количестве заказов за каждый месяц. Ключами словаря должны быть год-месяц в формате 
YYYY-MM
, а значениями - словари, содержащие два поля: 
average_order_value
 - средняя стоимость заказа за месяц, 
order_count
 - количество заказов за месяц."""