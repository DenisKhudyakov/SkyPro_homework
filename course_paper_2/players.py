
class Player:

    def __init__(self, name: str):
        """Инициализация класса игрок, создается его имя и создается пустой спискок"""
        self.name = name
        self.user_words = []

    def count_word(self) -> int:
        """Подсчет списка слов"""
        return len(self.user_words)

    def add_word(self, word: str) -> None:
        """Добавления слов в список"""
        self.user_words.append(word)

    def is_repeat(self, word: str) -> bool:
        """Проверка, чтобы пользователь не повторялся"""
        return word in self.user_words


    def __repr__(self):
        return f'Привет, {self.name.title()}!'
