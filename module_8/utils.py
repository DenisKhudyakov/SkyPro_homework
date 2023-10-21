from question import Question
import json

def load_random_question_and_word(user_answer=None) -> list:
    with open('question.json', 'r', encoding='utf-8') as file:
        data_base = json.load(file)
        return list(map(lambda choice_data: Question(choice_data['q'], choice_data['d'], choice_data['a'], user_answer=user_answer), data_base))



