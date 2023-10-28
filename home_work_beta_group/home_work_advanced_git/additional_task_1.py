from typing import Any


class Product:
    any_list = []

    def __init__(self, name: str, price: int, category: str, quantity: int):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity

    def product_data(self) -> dict[Any]:
        """
        Инициализация продуктового словаря
        :return: возврщаем заполненный словарь
        """
        return {
            "Наименование товара": self.name,
            "Стоимость": self.price,
            "Категория продукта": self.category,
            "Количество в наличии": self.quantity,
        }

    def product_data_list(self) -> list[dict[Any]]:
        """
        Заполняем статическую перменнут any_list
        :return: возвращаем заполненную статическуию переменную
        """
        self.any_list.append(self.product_data())
        return self.any_list

    @staticmethod
    def sort_product(any_list: list) -> list:
        """
        Функция должна возвращать список словарей,
        отсортированных по убыванию стоимости продукта,
        но только для продуктов из заданной категории.
        Если категория не задана, то сортировка производится для всех продуктов.
        """
        any_list = [i for i in any_list if bool(i['Категория продукта']) == True]
        return sorted(any_list, key=lambda price: price['Стоимость'], reverse=True)


moloko = Product("молоко", 10, "Молочка", 200)
moloko.product_data_list()
bread = Product("Хлеб", 30, "Хлебобулочные изделия", 300)
bread.product_data_list()
meat = Product("Мясо", 300, "Мясные изделия", 20)
meat.product_data_list()
print(Product.any_list)
print(Product.sort_product(Product.any_list))