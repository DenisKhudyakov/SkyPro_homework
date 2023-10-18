from utils import load_random_question_and_word

user_data = {}


if __name__ == '__main__':
    game = load_random_question_and_word()
    for i_game in game:
        print(f'Программа: {i_game.build_question()}')
        user_answer = input('Пользователь: ')
        user_game = load_random_question_and_word(user_answer=user_answer)
        print(i_game.feedback(user_answer))
