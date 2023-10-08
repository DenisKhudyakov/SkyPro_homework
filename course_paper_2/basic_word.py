import json

class BasicWord:
    list_of_additional_words = []
    count = 0
    def __init__(self, word):
        """
        Инициализация класса, на вход которого подается слово,
        и при инициализации класса мы загружаем в статический атрибут список возможных вариантов
        """
        self.word = word
        with open('words.json', 'r', encoding='utf-8') as file:
            filter_list = list(filter(lambda x: x['word'] == self.word, json.load(file)))
            self.list_of_additional_words = filter_list[0]['subwords']

    def is_there(self, user_import_word: str) -> bool:
        """метод проверки ответов пользователя"""
        return user_import_word in self.list_of_additional_words


    def count_words(self, user_import_word: str) -> int:
        """метод подсчета правильных вариантов"""
        if self.is_there(user_import_word):
            self.count += 1
        return self.count

    def __repr__(self):
        """магический метод преобразования данных объекта в строку"""
        return f'Составьте {len(self.list_of_additional_words)} слов из слова {self.word.upper()}'
