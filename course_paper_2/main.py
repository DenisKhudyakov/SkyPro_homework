from players import Player
from utils import load_random_word

user_input = ''

if __name__ == '__main__':
    print('Программа: Введите имя игрока')
    user_name = input('Пользователь: ')
    user = Player(user_name)
    print(f'Программа: {user}')
    word = load_random_word()
    print(f'Программа: {word}')
    print('Программа: Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print('Программа: Поехали, ваше первое слово?')
    while user_input != 'stop' and word.count_words() != 0 and user_input != 'стоп':
        user_input = input('Пользователь: ')
        if word.is_there(user_input):
            print('Программа: верно')
            user.add_word(user_input)
            word.list_of_additional_words.remove(user_input)
            continue
        elif user.is_repeat(user_input):
            print('Программа: уже использовано')
            continue
        elif len(user_input) < 3:
            print('Слишком короткое слово')
        else:
            print('Программа: не верно')
    print(f'Программа: Игра завершена, вы угадали {len(user.user_words)} слов!')



