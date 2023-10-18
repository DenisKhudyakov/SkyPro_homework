import json

class BasicWord:
    def __init__(self, word: str, subwords: list[str]):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.word}, {self.subwords})'



def utils():
    with open('file.json', 'r', encoding='utf-8') as file:
        data_base = json.load(file)
        return BasicWord(data_base['word'], data_base['subwords'])



