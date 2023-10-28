def list_with_pallindrome(input_list: list[str]) -> list:
    """
    :param input_list: подается список строк
    :return: в списке остаются только слова палиндромы
    """
    return list(filter(lambda x: x == x[::-1], input_list))
    # return list(filter(lambda x: x[-1:] == x[0], input_list)) почитал ТЗ достаточно сравнивать первую и последюнюю букву


print(list_with_pallindrome(["hello", "world", "apple", "pear", "banana", "pop"]))
