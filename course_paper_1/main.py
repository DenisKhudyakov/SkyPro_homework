from morse_code import code_dict
import random

answers = []

def morse_encode(any_word: str) -> str:
    """Переводчик латинского
    слова в код азбуки Морзе
    """
    return ''.join([code_dict.get(i) for i in any_word])

def get_word() -> str:
    """Данный метод рандомно возвращает
    слово из списка words,
    который заранее подготовлен
    по ТЗ функция get_word без переменных
    """
    words = ['woman', 'car', 'gun', 'python', 'pussy']
    return random.choice(words)

def print_statistics(answers: list) -> None:
    print('Всего задачек: {count_list}\nОтвечено верно: {count_true}\nОтвечено неверно: {count_false}'.format(
        count_list=len(answers),
        count_true=len(list(filter(lambda x: x == True, answers))),
        count_false=len(list(filter(lambda x: x == False, answers)))
    ))
# Основной код:
if __name__ == '__main__':
    print('Сегодня мы потренируемся расшифровывать морзянку.\nНажмите Enter и начнем')
    user = input('Пользователь ')
    print()
    for i in range(5):
        word = get_word()
        print(f'Программа:\nСлово {i+1} - {morse_encode(word)}')
        answer_user = input('Пользователь:\n').lower()
        answers.append(answer_user == word)
        print(f'Верно, {word}!' if answer_user == word else f'Неверно, {word}!')
    print()
    print_statistics(answers)

