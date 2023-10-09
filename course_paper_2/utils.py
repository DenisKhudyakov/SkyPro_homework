import json, random
from basic_word import BasicWord
def load_random_word():
    with open('words.json', 'r', encoding='utf-8') as file:
        data_base = json.load(file)
        random_word = random.choice([i["word"] for i in data_base])
        filter_list = list(filter(lambda x: x['word'] == random_word, data_base))
        list_of_additional_words = filter_list[0]['subwords']
        return BasicWord(random_word, list_of_additional_words)