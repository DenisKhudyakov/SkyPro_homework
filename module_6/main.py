from pathlib import Path
import random
score = 0
players_dict = {}

# Создание и запись файла word.txt
words_list = ['python', 'squirrel', 'flask', 'cucumbers']
with open('words.txt', 'w') as file:
    file.write('\n'.join(words_list))


def random_word() -> str:
    with Path('words.txt').open('r') as f:
        return random.choice(f.read().split())


if __name__ == '__main__':
    print('Программа: Введите ваше имя ')
    name_user = input('Пользователь: ')
    players_dict[name_user] = score
    for i in range(2):
        word = random_word()
        mix_word_list = list(word)
        random.shuffle(mix_word_list)
        print(f'Программа: Угадайте слово: {"".join(mix_word_list)}')
        answer_user = input('Пользователь: ')
        print('Программа: Верно! Вы получаете 10 очков.' if answer_user == word else f'Программа: Неверно! Верный ответ – {word}.')
        players_dict[name_user] += 10



    with open('history.txt', 'a', encoding='utf-8') as file:
        for user, i_score in players_dict.items():
            file.write(f'{user} {i_score}\n')

    with open('history.txt', 'r', encoding='utf-8') as file:
        games = len(file.read().rstrip().split('\n'))
        print(f'Всего игр сыграно: {games}')
        print(f'Максимальный рекорд: {max(players_dict.values())}')