import json, random
from basic_word import BasicWord
def load_random_word():
    with open('words.json', 'r', encoding='utf-8') as file:
        random_word = random.choice([i["word"] for i in json.load(file)])
        return BasicWord(random_word)