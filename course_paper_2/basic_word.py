import json

class BasicWord:
    def __init__(self, word, list_of_additional_words):
        """
        Инициализация класса, на вход которого подается слово,
        и при инициализации класса мы загружаем в статический атрибут список возможных вариантов
        """
        self.word = word
        self.list_of_additional_words = list_of_additional_words

    def is_there(self, user_import_word: str) -> bool:
        """метод проверки ответов пользователя"""
        return user_import_word in self.list_of_additional_words


    def count_words(self) -> int:
        """подсчет количетсва слов в списке"""
        return len(self.list_of_additional_words)


    def __repr__(self):
        """магический метод преобразования данных объекта в строку"""
        return f'Составьте {len(self.list_of_additional_words)} слов из слова {self.word.upper()}'
