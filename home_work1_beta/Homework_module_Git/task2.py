from functools import reduce


def multiplication(list_number: list[int]) -> int:
    """
    :param list_number: на вход подается список с числами, нужно умножить два максимальных значения
    :return: выход целое число, полученное из списка чисел
    """
    return reduce(lambda x, y: abs(x * y), list_number[-2:])


print(multiplication([-5, -7, -9, -13]))
print(multiplication([2, 3, 5, 7, 11]))
